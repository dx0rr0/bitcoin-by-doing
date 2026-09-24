# Session 1 · Where are the bitcoins?

[Previous: session 0](00-getting-started-together.md) · [Course outline](README.md) · [Next: session 2](02-following-a-payment.md)

**Question:** when a wallet displays a balance, what data lets it calculate that number?

**Starting point:** the regtest node from session 0, a working Python query, and preserved local state. We do not assume wallets or funds exist yet.

**What you'll build:** your own way to list a wallet's available outputs and calculate a total you can cross-check. You choose the code and how to present the data.

## Predict before querying

1. If you create a wallet and then several addresses, will any bitcoin appear?
2. Are a wallet and an address the same thing?
3. Do you think the balance is a stored number that increases and decreases, or can it be reconstructed from other data?

Keep your initial answer even if it changes later.

## Guided experiment

1. Create two lab wallets, Alice and Bob, using the node's documentation. Confirm that queries target the wallet you intend to observe.
2. Obtain addresses and inspect the initial state. Keep an observation from before generating funds.
3. Generate one regtest block with its reward going to Alice, and inspect the balance categories.
4. Find out why seeing a reward does not mean you can spend it immediately. Generate the necessary blocks and compare the categories again.
5. Identify the outputs the wallet offers as available. Pick one and describe the fields that distinguish it from every other output.
6. Decide which set of outputs your program will sum: confirmations, spendability, and other filters should be explicit.
7. Write the calculation in Python and compare it with a Bitcoin Core query that measures the same thing. If the totals differ, investigate which outputs are included before changing the arithmetic.

For this first case, the tutor will help keep the wallets simple, using local test keys. Watch-only wallets, multisig, and external funds come later.

## A little vocabulary, after observing

An **output** specifies an amount and spending conditions. A later transaction can consume it. A **UTXO** is a transaction output that remains unspent.

A wallet knows about keys, descriptors, and transactions relevant to it. Its balance depends on which outputs it considers its own and its rules for including them. A wallet's list is not the entire network's UTXO set.

The **coinbase** is the special transaction that creates a block's reward; this does not refer to a company. It has a maturity rule. Don't infer from this exception that all payments require the same wait.

## A variation

Choose one small check with the tutor:

- Request another Alice address and predict the effect on the balance.
- Compare Alice and Bob, explaining the difference using specific outputs.
- Change the confirmation filter and explain the new total.

## Completion check

Using your own program's output, you should be able to:

- Identify an output by its transaction and position within that transaction.
- Explain what you summed, in which units, and what you excluded.
- Distinguish immature rewards, available funds, and another wallet's balance.
- Draw a wallet with multiple addresses and outputs without representing it as a single bank account.

Save your code and a [short note](session-template.md). Keep the lab intact: Alice will need funds for session 2. Record the height, wallets used, and filters without exporting their keys.

<details>
<summary>Hints if you get stuck</summary>

- Search RPC help for wallet operations. `listunspent` and `getbalances` answer related questions, but do not always include the same set of outputs.
- Select the wallet explicitly when more than one is loaded.
- On a new chain, generating 101 blocks is a common way to make a mature reward available to a wallet. Also observe how many rewards remain immature; don't apply this waiting period to an ordinary payment.
- An empty list may be caused by filters or maturity. It does not by itself prove that the wallet has lost information.
- Avoid converting amounts to `float` first and fixing the error afterward. Investigate an exact representation from the point where you read the data.

</details>

## References

- [Wallet outputs: listunspent](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/listunspent/).
- [Balance categories: getbalances](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/getbalances/).
- [Rewards and regtest setup](https://developer.bitcoin.org/examples/testing.html#regtest-mode).

RPC names are references, not prescribed interfaces for your program. Check their options against the installed version's help.
