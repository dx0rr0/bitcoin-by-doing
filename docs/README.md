# Course outline and depth

[Home](../README.md) · [Learning method](learning-method.md) · [Progress](progress.md)

The goal is to follow a payment, explain the relevant rules, and design experiments to check them. Elliptic curve mathematics is not an entry requirement.

## Session map

| Stage | Session | Question | What we'll aim for |
| --- | --- | --- | --- |
| Preparation | [0. Getting started together](00-getting-started-together.md) | What do I need to experiment? | A chosen and verified environment, understood startup and shutdown steps, and a first read-only query. |
| Observe | [1. Where are the bitcoins?](01-where-are-the-bitcoins.md) | Where does the balance come from? | Your own UTXO inventory and an explanation of balance categories. |
| Observe | [2. Following a payment](02-following-a-payment.md) | What gets consumed and what gets created? | A reconstruction of a transaction and its fee from the underlying data. |
| Observe | [3. From pending to confirmed](03-from-pending-to-confirmed.md) | What changes when a transaction enters a block? | Before-and-after observations and tracking from Python. |
| Test assumptions | 4. Conflicting spends | What prevents double spending? | Two spends of the same UTXO; distinguish mempool policy from consensus rules. |
| Test assumptions | 5. Signatures and spending conditions | What does a signature authorize? | Sign with existing tools and observe a modification that invalidates authorization. Understand the roles of Script and witness. |
| Implement | 6. Bytes and transactions | What travels across the network? | Your own parser for a limited transaction format, compared with Core. Explicit limits regarding SegWit and other formats. |
| Implement | 7. Headers and work | What does mining mean? | Parse a header and check its hash against the target. A simple nonce-search experiment. |
| Connect | 8. Nodes and competing branches | How do different histories converge? | Two regtest nodes, controlled branches, and a reorganization based on accumulated work. |

Sessions 0–3 have full guides. Sessions 4–8 are learning goals; their guides will be written around the questions that come up. There are no links to lessons that do not exist yet.

## How deep we'll go

By the end, we'll aim for you to be able to:

- Explain wallets, keys, addresses, UTXOs, transactions, mempools, blocks, and nodes without treating them as interchangeable.
- Query and control local nodes from Python, read errors, and repeat an experiment.
- Trace transaction amounts back to the previous outputs being spent.
- Understand the purpose of signatures, spending conditions, and hashes, using existing cryptographic implementations.
- Implement small pieces of serialization and verification, stating which formats they support.
- Distinguish consensus rules, node policy, and wallet decisions.
- Read a simple functional test and propose a variation that checks a behavior.

Mathematical proofs of cryptographic security, a complete consensus implementation, Taproot in depth, Lightning, advanced privacy, and wallet security are outside these eight sessions. They can become separate learning paths later.

## Pace and completion

A session is a unit of learning, not a requirement to finish in one afternoon. Setting aside 60–90 minutes is a reasonable starting point; installation, debugging, or curiosity may take longer. A session can span several meetings.

Moving on requires a reproducible observation and your own explanation. Reading a file or seeing a script work is not enough. The [shared method](learning-method.md) explains how to check understanding without turning it into an exam.

Afterward, there is a [bridge to open source](contributing-to-open-source.md): learn to build and test a real repository, read its code, and contribute a reproduction or a small test. Completing the course does not guarantee that a contribution will be accepted.
