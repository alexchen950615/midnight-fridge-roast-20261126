# Midnight Fridge Roast

[![make.fun · Midnight Fridge Roast](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/alexchen950615/midnight-fridge-roast-20261126/rank.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/alexchen950615/midnight-fridge-roast-20261126/reward.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

An entry for the [make.fun](https://make.fun) bounty **"Midnight Fridge Roast"** — one funny line roasting a smart fridge that refuses to open after midnight. The fridge has turned into a nightclub bouncer, and the punchline is the twist: the leftovers made the list, the owner didn't.

## The entry

> My fridge locks itself at midnight like a bouncer — the leftovers are on the list, I'm not.

91 characters, one line. The midnight lock is the target, the bouncer is the setup, and the list reversal is the punchline — spoken like something you'd actually mutter at the fridge door at 12:05 a.m.

## How it works

`main.py` writes the entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with a built-in assertion gate (1–200 characters, single line, not only whitespace) that fails loudly if the gate would fail. Deterministic — every run writes the same text. Stdlib only, no network.

```sh
python3 main.py
cat /output/entry.txt
```
