# yap

A Claude Code skill that runs one talking-head video rep, start to finish, without writing a
single line for you.

The premise: for your first 25 to 30 videos, you have to write the words yourself or you never
learn what good looks like. Claude is very good at research, data, structure, fact-checking
and honest grading. It is bad at writing your script. This skill puts Claude on the first list
and keeps it off the second.

## What it does

Seven stages, one rep per chat:

1. **Topic.** Pulls your outlier data (videos that did several times a channel's normal), flags
   what fits your audience and what does not, and runs the take test with you. No take from
   you, no video.
2. **Scaffold.** Pulls the section structure of an analysed source video and lists your
   receipts, every number checked against its file. No lines.
3. **Write.** You write, section by section. Claude grades each line against a fixed clarity
   bar and tells you exactly which sentence fails and why.
4. **Gate report.** Fourteen pass or fail gates, including a slop check for AI writing
   habits that creep into hand-written lines. Failures block filming.
5. **Film card.** Prompter, three takes, setup.
6. **Edit build.** Element by element, sound last, volume rules that override everything.
7. **Log.** The rep goes in the log. Sunday numbers re-aim next week.

## Install

Copy this folder to your skills directory:

```bash
# project-level (recommended)
cp -r yap-skill/ your-project/.claude/skills/yap/
```

```bash
# or user-level, available in every project
cp -r yap-skill/ ~/.claude/skills/yap/
```

Then create a `yap/` folder in your project root from the templates:

```bash
mkdir -p your-project/yap/feedback && cp yap-skill/templates/*.md your-project/yap/
```

Fill in `yap/audience-map.md` and `yap/offer.md` before your first rep. The skill stops if
either file is missing. It does not check whether they are filled in, so do it: a blank
audience map gives the take test nothing to aim at, and a blank offer gives the fact gate
nothing to check against.

## Run

In Claude Code, inside your project:

```
/yap
```

Or say "next rep", "rep 4", "let's do a yap". One rep per chat. Open a new chat for the next
one. Standing context lives in the `yap/` files, not in conversation history.

## Outlier data: connect Sandcastles

Stage 1 needs outlier videos, and Stage 2 needs the section structure of one. The skill does
not scrape Instagram. It gets that data from Sandcastles (sandcastles.ai), a research tool
that tracks a watchlist of channels, ranks every video against its own channel's normal, and
holds analysed breakdowns with timestamped sections. With it connected, the skill pulls your
watchlist itself. Without it, you paste the list by hand (see below).

**You need a paid Sandcastles plan.** The MCP is included on Pro, Visionary and Titan. Starter
does not have it; upgrade under Settings, Subscription, and the plugin download appears.

**Setup, once, about two minutes.** The full walkthrough with screenshots is at
https://sandcastles.ai/mcp. In short:

1. In Sandcastles: Settings, Connectors, MCP section, download the plugin zip.
2. In the Claude desktop app (claude.com/download, the browser chat cannot do this):
   Customize, Plugins, Add, Upload Plugin, drop the zip in. Then press Connectors on the
   Plugins page and Install. Click Add on the connector window. It can look like nothing
   happened. It did.
3. Connectors in the left nav, find Sandcastles, click Connect, log in once in the tab that
   opens. If no tab opens it is a pop-up blocker.
4. Set the tool permissions to Always allow, or Claude stops to ask mid-rep.
5. Ask Claude for the top videos on your watchlist. Real data back means it worked.

Once connected on your account, the Sandcastles tools show up in Claude Code sessions too.

**Credits.** Reading your watchlist is free. Running a deep analysis on a video spends a
credit. The skill asks for your explicit yes on the number before it spends one, every time.

**No Sandcastles?** Paste a list: video link, views, and the channel's normal (median views of
its last 20 to 30 posts, outliers left out). Claude computes the multiple and judges. For the
scaffold, paste the source video's transcript with timestamps and Claude sections it.

Rule either way: only a video at 5x or more of its channel's normal can donate structure.

## The rules in short

- Claude never writes lines, hooks, or captions. Ask it to and it will tell you once, plainly,
  to use ChatGPT if you want the words written for you, then go back to asking you questions.
- Claude prompts you with questions before every section, three at most, then grades what
  you write. You do the talking.
- Bring a video that broke out and it teaches you why, in plain words, before anything else:
  the multiple, who it was for, the first two lines, the turn, the proof, the shape, the
  close, and which of those you can actually do on your account.
- No cheerleading. Verdicts come with reasons.
- One stage at a time. Claude waits for you at every boundary.
- Post one a day while testing. Ramp only after a provable breakout.
- Text hook and spoken hook are the same words.
- Every number is traced to a file before it goes in a video.
- On a small account the proof has to be in the video, not on the profile.
- Sound effects last, quiet, and never on the last word of a line.
- Three or more AI writing tells in a script fails the gate, hand-written or not.

## Files

```
SKILL.md                     the skill
templates/audience-map.md    who the content is for
templates/offer.md           what the content must stay congruent with
templates/rep-log.md         the log
templates/edit-checklist.md  your edit order and sound rules
examples/worked-rep.md       one illustrative rep that got through, invented account
examples/worked-rep-skipped.md  one that died at the gate, and what she did instead
```

Read the skipped one first. Most reps end there, and that is the skill working.

## Testing it

If something breaks, or the skill does something the rules above say it should not (writes a
line for you, cheerleads, skips a stage), open an issue on this repo. Paste the stage you were
on and what it said. That is the most useful thing a tester can send.

## Licence

MIT. Use it, change it, share it. See `LICENSE`.
