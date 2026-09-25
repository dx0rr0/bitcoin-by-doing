# Progress

[Course outline](README.md) · [Note template](session-template.md)

Prepared guides do not represent completed exercises. The initial state does not assume an installed environment or demonstrated understanding.

| Session | Material | Observed execution | Explanation and variation | Learner's note |
| --- | --- | --- | --- | --- |
| 0 | Ready | Regtest node, Python query, stop, and restart observed | Learner explained CLI versus node and confirmed state persistence | [session-00.md](../notes/session-00.md) |
| 1 | Ready | At height 102, Alice `listunspent` sum = `getbalances.mine.trusted` = 100 BTC; Bob = 0 BTC | Learner identified outputs by `txid` and `vout`, explained coinbase maturity and the zero Bob balance; one-block variation changed Alice total from 50 to 100 BTC | [session-01.md](../notes/session-01.md) |
| 2 | Ready | Pending | Pending | — |
| 3 | Ready | Pending | Pending | — |
| 4 | Goal defined | Pending | Pending | — |
| 5 | Goal defined | Pending | Pending | — |
| 6 | Goal defined | Pending | Pending | — |
| 7 | Goal defined | Pending | Pending | — |
| 8 | Goal defined | Pending | Pending | — |

## Next step

Start session 2 by tracing a payment from Alice to Bob. Keep the regtest state at height 102 and use the existing wallets.

## Questions to revisit

These will be added during the sessions, using the learner's own words where possible.
