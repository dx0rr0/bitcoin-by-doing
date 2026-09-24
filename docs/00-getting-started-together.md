# Session 0 · Getting started together

[Course outline](README.md) · [Learning method](learning-method.md) · [Next: session 1](01-where-are-the-bitcoins.md)

**Question:** what do I need to experiment with Bitcoin, and how do I know what's running?

Work through this session in conversation with the tutor. This document is an agenda, not an installation sequence you are expected to guess. By the end, you will have a local test node and know how to query, stop, and restart it.

## Before installing anything

Describe what you tried in *Programming Bitcoin*, what feels familiar, and where you got lost. Then we check your current environment:

- Your operating system and preferred terminal.
- Available Python and Git installations, their versions, and how to run them.
- Whether you already have Bitcoin Core, Docker, or WSL, and how comfortable you are with them.
- Where you will keep the repository and lab state.

You don't need to master Docker or learn Linux at the same time. On Windows, we choose between native binaries, WSL, or a container based on what you already use. We pick one route and record the actual instructions after verifying them.

## Decisions we'll make

| Decision | What we need to establish |
| --- | --- |
| Installation | Get Bitcoin Core from its official distribution and verify it using the published instructions. Record the chosen version. |
| Network | Use regtest and demonstrate that choice by querying the node. |
| Data | Use a dedicated directory under `.local/`, outside Git and separate from any personal installation. |
| Access | Keep RPC local. Understand how queries authenticate without copying credentials into code or notes. |
| Python | Choose an environment and dependencies only as needed. Calling a command-line process or making an RPC request are options; there is no prebuilt client. |
| Organization | Decide together where the first experiment belongs and how to run it. Don't design every session upfront. |

The tutor can resolve installation problems and explain commands. Before an operation, you should know which component it affects and how to check the result.

## First experiment

1. Start the node with the configuration we chose.
2. Query its network and chain height. Save only the fields you understand and need.
3. Identify which process responds and which file or setting selected the network.
4. Make a read-only query to the same node from Python. Choose how to do it, with help if the connection gets in the way.
5. Shut down the node cleanly and try querying it again. Distinguish a connection failure from an error returned by Bitcoin Core.
6. Restart it with the same data directory and check that it responds.

We are not building a generic client or adding retries, classes, or a custom API yet. The first query can fit in a very small file.

## What you should be able to explain

- How do Bitcoin Core, the command-line tool, your script, and a wallet differ?
- Why doesn't this node need to download the public blockchain?
- Which piece of data proves you are using regtest?
- What does the data directory preserve, and what would you lose by deleting it?
- What would you change to repeat the lab from scratch while keeping the previous one?

You don't need all the answers before starting. We'll work them out by seeing the components in action.

## What to record

A note with versions, installation location, local state location, verified startup and shutdown steps, and the next action. Replace personal paths with placeholders before publishing if you don't want to share them. Do not include cookies, passwords, or wallet files.

You write the query code. If the tutor had to write an incidental part, record which part and what you understand about it.

**Completion check:** you can restart the node, demonstrate its network, and query it from Python without the tutor repeating the full sequence for you. The initial course progress stays pending until you perform these checks.

## References to consult together

- [Official Bitcoin Core downloads](https://bitcoincore.org/en/download/).
- [What regtest provides](https://developer.bitcoin.org/examples/testing.html#regtest-mode). This page includes older examples; check parameters against the installed help.
- [Chain information, Core 30.0](https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/getblockchaininfo/).
- [How to use versions and references](resources.md).
