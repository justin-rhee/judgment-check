# judgment-check

[![tests](https://github.com/justin-rhee/judgment-check/actions/workflows/test.yml/badge.svg)](https://github.com/justin-rhee/judgment-check/actions/workflows/test.yml) [![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) ![format: agent skills](https://img.shields.io/badge/format-agent%20skills-blue.svg) ![nothing to install](https://img.shields.io/badge/runs-nothing%20in%20the%20background-brightgreen.svg)

Three short checklists for agent work: write down a guess before you know the answer, turn a lesson into one small change, and move a session to a new model without losing your place.

| Habit | What it guides |
| --- | --- |
| [judgment-loop](skills/judgment-loop/SKILL.md) | prediction records, independent scores and evidence-only reviews |
| [scale-the-lesson](skills/scale-the-lesson/SKILL.md) | capture, authority boundaries and review of proposed changes |
| [agent-model-migration](skills/agent-model-migration/SKILL.md) | scoped configuration, uninterrupted work and migration evidence |

They started as my own working files, written against my ledger, my commands and my handoff paths. I took those out, so what's left runs on whatever record and runtime you already have. The only thing they change is what you write down.

## Use it if

- you want predictions written down before anyone knows the outcome
- a lesson has to land somewhere without becoming an automatic rule change
- a model trial needs a baseline, a check and a way back

## Install

Each habit is one Markdown file of 300 to 450 words. Copy the folders into the one your agent loads skills from, `~/.claude/skills` or `.claude/skills` for Claude Code:

```sh
git clone https://github.com/justin-rhee/judgment-check
mkdir -p ~/.claude/skills
cp -R judgment-check/skills/* ~/.claude/skills/
```

Review any folder with the same name before replacing it. They also read fine as plain checklists with nothing installed. Check the install with your agent's own loader, since the tests here don't exercise Claude Code.

## What it won't do

- enforce tool permissions, make a reviewer independent or prove a model is calibrated, since it's text
- cut off access for a blind review; the host has to do that
- grant new authority to buy, restart, send or change shared settings

## How I tested it

- six offline tests: `bash tests/run.sh`
- they load the three habits, install them into an empty folder from a separate directory, and reject a habit with no description or one pointing outside the bundle
- removing the description check makes its rejection test fail; CI runs Python 3.10 and 3.13, and [TEST-RESULTS.md](TEST-RESULTS.md) records the scope

## License

MIT. See [LICENSE](LICENSE). No warranty. Security notes and how to report a problem: [SECURITY.md](SECURITY.md).

<!-- related:start -->
## Related

- [scar-audit](https://github.com/justin-rhee/scar-audit): shows which written rules your agent quietly skips
- [linter-selftest](https://github.com/justin-rhee/linter-selftest): proves each lint rule can still fire

Part of a small set of tools I pulled out of my own agent harness. I use them myself and read every issue. More on my [GitHub profile](https://github.com/justin-rhee).
<!-- related:end -->
