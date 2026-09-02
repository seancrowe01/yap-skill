#!/usr/bin/env python3
"""Download a short video from a URL, transcribe it with timestamps, print caption and
transcript, delete the media. Used by the yap skill when no research tool is connected.

Needs: yt-dlp, ffmpeg on PATH, and GROQ_API_KEY in the environment.
Usage: python scripts/get-transcript.py <video url>
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import uuid


def die(msg, fix=None):
    print(f"ERROR: {msg}")
    if fix:
        print(f"FIX: {fix}")
    sys.exit(1)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(sys.argv) < 2:
        die("no url given", "python scripts/get-transcript.py <video url>")
    url = sys.argv[1]

    if not shutil.which("yt-dlp"):
        die("yt-dlp not found", "pip install yt-dlp   (or: brew install yt-dlp)")
    if not shutil.which("ffmpeg"):
        die("ffmpeg not found", "winget install ffmpeg   (or: brew install ffmpeg)")
    key = os.environ.get("GROQ_API_KEY", "").strip()
    if not key:
        die("GROQ_API_KEY not set",
            "free key at console.groq.com, then set GROQ_API_KEY in your environment")

    work = tempfile.mkdtemp(prefix="yap-")
    base = os.path.join(work, "src")
    try:
        r = subprocess.run(
            ["yt-dlp", "--no-playlist", "-o", base + ".%(ext)s", "--write-info-json", url],
            capture_output=True, text=True)
        if r.returncode != 0:
            die("download failed", r.stderr.strip().splitlines()[-1] if r.stderr else "check the url")

        info = {}
        info_path = base + ".info.json"
        if os.path.exists(info_path):
            with open(info_path, encoding="utf-8") as f:
                info = json.load(f)

        media = next((os.path.join(work, n) for n in os.listdir(work)
                      if n.startswith("src") and not n.endswith(".json")), None)
        if not media:
            die("no media file after download")

        audio = os.path.join(work, "audio.mp3")
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", media, "-vn", "-ac", "1",
                            "-ar", "16000", "-b:a", "48k", audio], capture_output=True, text=True)
        if r.returncode != 0:
            die("audio extraction failed", r.stderr.strip())

        boundary = uuid.uuid4().hex
        with open(audio, "rb") as f:
            audio_bytes = f.read()

        def part(name, value):
            return (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n"
                    f"{value}\r\n").encode()

        body = b"".join([
            part("model", "whisper-large-v3-turbo"),
            part("response_format", "verbose_json"),
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
            f"filename=\"audio.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n".encode(),
            audio_bytes, b"\r\n", f"--{boundary}--\r\n".encode(),
        ])
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/audio/transcriptions", data=body, method="POST",
            headers={"Authorization": f"Bearer {key}",
                     "User-Agent": "yap-skill/1.0",
                     "Content-Type": f"multipart/form-data; boundary={boundary}"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            die(f"transcription request failed: {e}")

        dur = None
        try:
            p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", media], capture_output=True, text=True)
            dur = float(p.stdout.strip())
        except Exception:
            pass

        print("SOURCE")
        print(f"url: {url}")
        print(f"account: {info.get('uploader') or info.get('channel') or '[GAP]'}")
        print(f"posted: {info.get('upload_date') or '[GAP]'}")
        print(f"duration_seconds: {round(dur, 1) if dur else '[GAP]'}")
        print(f"views: {info.get('view_count') if info.get('view_count') is not None else '[GAP], ask the user'}")
        print(f"likes: {info.get('like_count') if info.get('like_count') is not None else '[GAP]'}")
        print(f"comments: {info.get('comment_count') if info.get('comment_count') is not None else '[GAP]'}")
        print("channel_normal: [GAP], ask the user for the median of the last 20 to 30 posts")
        print()
        print("CAPTION")
        print((info.get("description") or "[none]").strip())
        print()
        print("TRANSCRIPT")
        for s in data.get("segments", []):
            print(f"[{s['start']:.1f}-{s['end']:.1f}] {s['text'].strip()}")
        if not data.get("segments"):
            print(data.get("text", "[empty]"))
    finally:
        shutil.rmtree(work, ignore_errors=True)
        print()
        print("media deleted")


if __name__ == "__main__":
    main()
