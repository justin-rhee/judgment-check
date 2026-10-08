# judgment-workflow-skills

The original versions assumed my own ledger, command-line tools and handoff files. Copying those instructions to another machine would leave the reader with dependencies they didn't have.

I kept the procedures and removed those dependencies. These are three plain-text skills for recording judgments, turning findings into bounded changes, and moving an agent session to another model. They don't install tools or change your configuration.

## Use it if

- you want predictions recorded before their outcomes are known
- lessons need a destination without becoming an automatic policy change
- a model trial needs a baseline, verification and a way back

## The skills

| Skill | What it guides |
| --- | --- |
| [judgment-loop](skills/judgment-loop/SKILL.md) | prediction records, independent scores and evidence-only reviews |
| [scale-the-lesson](skills/scale-the-lesson/SKILL.md) | capture, authority boundaries and review of proposed changes |
| [seat-model-migration](skills/seat-model-migration/SKILL.md) | scoped configuration, uninterrupted work and migration evidence |

## Install

Each folder contains a complete `SKILL.md` with a name and description. A runtime that supports this format can load the folders from its documented skill directory. For a project using `.agents/skills`, the copy is:

```sh
mkdir -p .agents/skills
cp -R skills/judgment-loop .agents/skills/
cp -R skills/scale-the-lesson .agents/skills/
cp -R skills/seat-model-migration .agents/skills/
```

Existing folders with those names need review before replacement. The files can also be read as checklists without installing them. They use your existing record and runtime rather than supplying a writer, scheduler or model launcher.

## What it won't do

Text instructions cannot enforce tool permissions, make a review independent or prove that a model is calibrated. A host must enforce access restrictions when a blind review requires them. These skills grant no new authority to purchase, restart, send or change shared controls.

The tests check packaging and broken references, not whether an agent will follow the instructions. No comparative outcome study is claimed. Only macOS has been tested locally. The included CI matrix has not run on a public repository yet.

## How I tested it

```sh
bash tests/run.sh
```

Six offline tests load the selected skills, copy them into an empty install directory, and reject missing discovery fields or references outside the bundle. Removing the description check makes its rejection test fail. [TEST-RESULTS.md](TEST-RESULTS.md) records the test scope.

## License

MIT. See [LICENSE](LICENSE). No warranty. [Security policy](SECURITY.md).

This little tool is one of a handful I pulled out of my own day-to-day agent setup. I use them all myself, so when something breaks I usually notice fast. But if you spot something weird, or just want to ask how it works, open an issue. I read every one. More tools on my [GitHub profile](https://github.com/justin-rhee).
