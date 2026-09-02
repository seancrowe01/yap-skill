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

## Outlier data

The skill works best with a content research tool connected over MCP (Sandcastles is one that
exposes watchlists and analysed video sections). It is optional. Without one, paste a list of
videos with their views and the channel's usual views, and Claude computes the multiple.

Rule either way: only a video at 5x or more of its channel's normal can donate structure.

## The rules in short

- Claude never writes lines, hooks, or captions.
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
examples/worked-rep.md       one illustrative rep, invented account
```

## Testing it

If something breaks, or the skill does something the rules above say it should not (writes a
line for you, cheerleads, skips a stage), open an issue on this repo. Paste the stage you were
on and what it said. That is the most useful thing a tester can send.

## Licence

MIT. Use it, change it, share it. See `LICENSE`.
