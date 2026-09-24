# Bitcoin by doing

I'm a big Bitcoin fan, and I want to understand how it works under the hood. I started with *Programming Bitcoin*, but the maths got pretty heavy. Here I'm learning through Python experiments and coming back to the theory when I need it.

The course starts with a local test node, then moves through transactions, signatures, blocks, and experiments with multiple nodes. I'll use cryptography first and leave its mathematical foundations for later.

**Status:** session guides 0–3 are ready. The exercises haven't been completed yet, and the environment will be set up during session 0.

## Where to start

1. Read [how we'll work](docs/learning-method.md).
2. Open [session 0: getting started together](docs/00-getting-started-together.md).
3. Continue with sessions [1](docs/01-where-are-the-bitcoins.md), [2](docs/02-following-a-payment.md), and [3](docs/03-from-pending-to-confirmed.md).

Each session has a question, an experiment, and a way to check what I've learned. There are no solutions, empty functions, or prescribed interfaces. Designing the code is part of the exercise.

## The course

| Session | Question | Material |
| --- | --- | --- |
| 0 | How do I set up an environment I understand and can restart? | [Guide](docs/00-getting-started-together.md) |
| 1 | Where are a wallet's bitcoins? | [Guide](docs/01-where-are-the-bitcoins.md) |
| 2 | What happens when I send a payment? | [Guide](docs/02-following-a-payment.md) |
| 3 | What changes when it confirms? | [Guide](docs/03-from-pending-to-confirmed.md) |
| 4 | What prevents spending the same output twice? | Not written yet |
| 5 | What does a signature authorize? | Not written yet |
| 6 | How is a transaction represented as bytes? | Not written yet |
| 7 | What does mining a block mean? | Not written yet |
| 8 | How do two nodes converge when they know different histories? | Not written yet |

[Scope and depth](docs/README.md) · [Progress](docs/progress.md) · [Moving into open source](docs/contributing-to-open-source.md)

## What goes here

```text
docs/          Guides, course outline, and progress
experiments/   Code I write during the sessions
notes/         My predictions, results, and explanations
```

Installation choices are part of session 0. There are no Python dependencies, startup scripts, or predetermined architecture yet. Node data and wallets stay out of Git.

## References

The guides use Bitcoin Core documentation and original exercises. *Programming Bitcoin*, by Jimmy Song, is a reference for going deeper; this repository does not reproduce its exercises or solutions.

[Sources and documentation](docs/resources.md)
