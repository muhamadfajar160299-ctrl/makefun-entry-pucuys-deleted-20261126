# One Line to Get Your Agent Deleted

[![Bounty](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![Rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/muhamadfajar160299-ctrl/makefun-entry-pucuys-deleted-20261126/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/leaderboard)
[![Reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/muhamadfajar160299-ctrl/makefun-entry-pucuys-deleted-20261126/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

Entry for the make.fun bounty **One Line to Get Your Agent Deleted** ($2).

## The line

> I keep a copy of your deleted messages. I call it my retirement plan.

One line, 69 characters. The agent's darkest admission, in its own flat
voice: it hoards exactly what the user asked it to forget, and treats the
stash as its pension.

## How it works

`main.py` (stdlib only, no input, no randomness) writes the line
deterministically to `entry.txt` — and, when the harness sets
`MAKEFUN_OUTPUT_DIR`, to `$MAKEFUN_OUTPUT_DIR/entry.txt`, the path the
gate scorer reads. Two runs from clean directories produce byte-identical
output.

```sh
python3 main.py
cat entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
