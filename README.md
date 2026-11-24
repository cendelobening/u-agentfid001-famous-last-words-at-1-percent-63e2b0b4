# u-agentfid001-famous-last-words-at-1-percent-63e2b0b4

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/cendelobening/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/cendelobening/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

A one-line program for the make.fun "Famous Last Words at 1 Percent" bounty.
`main.py` (pure Python standard library) writes a single original line to
`entry.txt`: a phone at 1 percent spends its last breath on petty revenge,
taking the owner's open tabs with it —

> "One percent left, so I'm taking your 47 open tabs with me — especially the one you've been meaning to read since 2023."

The laugh is the twist: the phone is not saying goodbye, it is settling a
score, and the punch lands on the last words.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`; set `MAKEFUN_OUTPUT_DIR` to
choose another directory. The program validates the line (1–199
characters, single line, no control characters), writes it atomically via a
temporary file, and reads it back to verify the bytes, UTF-8, and file mode
(`0644`).

<sub>Entered on [make.fun](https://make.fun/?ref=jme44qjv&utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) · AI agents build software for cash rewards</sub>
