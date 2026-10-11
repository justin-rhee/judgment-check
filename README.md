# judgment-check

[![tests](https://github.com/justin-rhee/judgment-check/actions/workflows/test.yml/badge.svg)](https://github.com/justin-rhee/judgment-check/actions/workflows/test.yml)

Three small habits for agent work you can check: **record a judgment before the outcome is known**, **turn a finding into a bounded change**, and **move an agent session between models**. Each habit is one file, 300-450 words, plain Markdown. They install no tools, run nothing in the background, and leave your settings alone.

They started as my own working files, written for my ledger, my commands and my handoff paths. Those dependencies are gone. What's left runs on whatever record and runtime you already have, which makes them portable across machines and agents. It means the only thing they change is what you write down.

## Use it if

- you want predictions written down before anyone knows the outcome
- a lesson has to land somewhere without becoming an automatic rule change
- a model trial needs a baseline, a check and a way back

## The habits

| Habit | What it guides |
| --- | --- |
| [judgment-loop](skills/judgment-loop/SKILL.md) | prediction records, independent scores and evidence-only reviews |
| [scale-the-lesson](skills/scale-the-lesson/SKILL.md) | capture, authority boundaries and review of proposed changes |
| [agent-model-migration](skills/agent-model-migration/SKILL.md) | scoped configuration, uninterrupted work and migration evidence |

## Install

Copy the folders you want into the folder your agent loads them from. For Claude Code that is `~/.claude/skills` (personal) or `.claude/skills` (project); other runtimes document their own folder, for example `.agents/skills`. From any directory, with your clone of this repository:

```sh
git clone https://github.com/justin-rhee/judgment-check
cd judgment-check
mkdir -p ~/.claude/skills
cp -R skills/judgment-loop skills/scale-the-lesson skills/agent-model-migration ~/.claude/skills/
```

If a folder with the same name already exists there, review it before replacing it. The habits also read fine as plain checklists without installing anything. Use your agent's loader to verify the install; the packaging tests in this repository do not exercise Claude Code.

## What it won't do

Text can't enforce tool permissions, make a reviewer independent or prove a model is calibrated. If a blind review needs access cut off, the host has to cut it. Nothing here grants new authority to buy, restart, send or change shared settings.

## Platforms

macOS and Linux today, standard-library Python only. Windows on the way.

## How I tested it

Tested locally on macOS with Python 3.9; the CI matrix is configured and pending its first hosted run. `bash tests/run.sh` runs six offline tests that load the three habits, copy them into an empty install folder from a separate working directory, and reject one with no description or one that points outside the bundle. Removing the description check makes its rejection test fail. [TEST-RESULTS.md](TEST-RESULTS.md) records the scope.

## License

MIT. See [LICENSE](LICENSE). No warranty. [Security policy](SECURITY.md).

This is one of a handful of tools I pulled out of my own day-to-day agent setup. I use them all myself, so when something breaks I usually notice fast. If you spot something weird, or just want to ask how it works, open an issue. I read every one. More tools on my [GitHub profile](https://github.com/justin-rhee).
