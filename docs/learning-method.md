# How we'll work

[Course outline](README.md)

You write the code and decide how to organize it. The tutor helps choose an experiment, understand the data, and work through obstacles. When reuse becomes useful, we decide what deserves a function or module.

## A session

1. **Resume.** Read the last note and check the node's state. Don't assume the lab is exactly as you left it.
2. **Predict.** Write two or three sentences about what you expect to observe. Being wrong here is useful.
3. **Learn what's needed.** A short explanation, real output, or a drawing. Further theory is available when needed, rather than being a prerequisite.
4. **Experiment.** Choose what to query or change and work in small steps. Understand one case first; then automate it in Python.
5. **Vary.** Change one condition and predict the effect before running it.
6. **Explain.** Describe what happened, which data supports it, and what remains unclear. Choose the next step together.

## Gradual help

If you get stuck, the tutor starts with a question about the missing data or assumption. Next comes a conceptual hint, a documentation section, or an operation name. A minimal example comes when those hints are not enough or when you ask for one.

There is no need to struggle with installation or memorize RPC parameters. Looking up documentation is a normal part of the work. Help with a Windows path should not also solve the Bitcoin exercise.

The expandable sections in the guides contain troubleshooting hints, not implementations. Leave them closed until you need them.

## What the experiments share

- A regtest node, separate local state, and versions recorded in session 0.
- Explicit units: BTC, satoshis, bytes, or vbytes as appropriate. Choose an exact representation for money.
- A prediction made beforehand, actual observations, and an independent cross-check where possible.
- Code written by the learner in `experiments/`. No required function names, output format, or framework.
- A short note in `notes/`, using the [template](session-template.md) if useful. Publish only lab excerpts without credentials.

Sessions 1–3 use the same lab. Restarting it does not mean resetting it: the node should retain its state. To repeat an experiment from scratch, use another data directory and record the change.

## How we know we're ready to move on

Each guide suggests checks. These are not automatic checkboxes: you explain real output and respond to a variation. If something only works by copying a sequence, we try a smaller example.

The [progress tracker](progress.md) separates **observed execution** from **explained understanding**. Questions can stay open and be revisited with more context.

## How to start with the tutor

> I want to work through session 0 of this repository. Read AGENTS.md and my progress. Guide me one step at a time: let me make decisions and run the experiments. Don't complete the whole course or give me the code interfaces.

For later sessions, change the number and add what you tried or the error you encountered. You don't need to paste the full conversation if your notes record the current state.
