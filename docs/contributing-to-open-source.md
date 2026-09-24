# From the course to a first contribution

[Course outline](README.md)

The eight sessions provide a practical foundation for understanding a bug reproduction and starting to read tests. Contributing also requires learning the chosen project's conventions, environment, and specific behavior.

You don't need to know everything before reviewing documentation or reproducing a problem. Nor should you assume that writing a useful test will take only one afternoon.

## Three steps into a project

| Step | Work | How to know you're ready to continue |
| --- | --- | --- |
| 1. Read and run | Choose a project, follow its development guide, and run a relevant test. In Core, read `example_test.py` and a functional test close to an experiment you've done. | Explain what it sets up, which action it takes, and what it checks. Be able to repeat it. |
| 2. Investigate a case | Find a bounded bug or a PR that needs testing. Check its current status and reproduce the behavior on an identified version. | Keep a minimal sequence, expected result, and observed result. Distinguish a product bug from an experiment error. |
| 3. Contribute | Write a reproduction, review a test, or propose a new one following the project's conventions. | Understand every assertion and explain the regression it detects. For a fix, check the case before and after where possible. |

Your first result can be a useful reproduction or a well-explained review. It does not depend on immediately finding a change the maintainers want to merge.

## Where Python fits

- **Bitcoin Core:** its functional tests use Python to control nodes and check RPC and P2P behavior. The product code is mostly C++; some bugs require reading or modifying it. [Test guide](https://github.com/bitcoin/bitcoin/blob/master/test/functional/README.md) and [commented example](https://github.com/bitcoin/bitcoin/blob/master/test/functional/example_test.py).
- **Electrum:** an option for exploring wallets in Python. You will need to learn its architecture and run its suite; the course does not cover all aspects of wallet security. [Contributing to Electrum](https://github.com/spesmilo/electrum#contributing).
- **Warnet:** network experimentation scenarios in Python. It adds containers and deployment knowledge and may make sense after the two-node experiment. [Scenarios](https://github.com/bitcoin-dev-project/warnet/blob/main/docs/scenarios.md).

We'll choose based on which parts of the course interest you. No issues are reserved and no external tasks are promised.

## Using AI when contributing

The tutor can help you understand a code fragment, locate documentation, or review a hypothesis. You must be able to explain the change, its tests, and its limits.

Bitcoin Core allows AI assistance under conditions: know the language, understand the code, and take responsibility as the human author. Its policy requires your own communication with maintainers and does not allow PRs driven by autonomous agents. Read the [current policy](https://github.com/bitcoin/bitcoin/blob/master/doc/AI_POLICY.md) before participating; other projects may have different rules.

## How to judge your readiness

When you can read a small test, predict its result, introduce a variation, and explain why it fails or passes, you have a starting point for investigating a contribution of that scope. That does not yet qualify you to review consensus, design cryptography, or audit a wallet.

The [PR Review Club](https://bitcoincore.reviews/) offers reading material and discussions about the review process. You can use its archives without committing to a scheduled activity.
