# Session 3 · From pending to confirmed

[Previous: session 2](02-following-a-payment.md) · [Course outline](README.md) · [Afterward: sessions 4–8](README.md#session-map)

**Question:** what exactly changes when a payment enters a block?

**Starting point:** the pending payment from session 2 and the same data directory. If it has already confirmed, record what happened and prepare an equivalent new payment. Never present a reconstructed state as a capture from the earlier experiment.

**What you'll build:** a small Python tracker that compares the same payment before and after generating blocks. You decide whether to use individual queries, a loop, or another approach. It does not need a web interface or a permanent service.

## Predict before generating a block

- Does Bob seeing the payment mean that it is confirmed?
- What do you expect to find in the node's mempool, and what in the chain?
- Which data will change after generating one block? What about another?
- Do you expect this payment's ID to change merely because it confirms?

## Set up a clear observation

Record the current height, the payment ID, and the wallets involved. Send rewards from new blocks to an address in a third lab wallet dedicated to mining. This keeps new rewards separate from the payment you are tracking in Alice and Bob.

If those wallets already contain older rewards, some may mature as the chain advances. The main subject of the experiment is therefore this transaction and its specific outputs, not just a change in total balance.

## Guided experiment

1. Observe the payment from Alice's wallet, Bob's wallet, and the node's mempool. Identify the question each query answers.
2. Save an initial observation before generating blocks. Distinguish chain information from local information about pending transactions.
3. Generate one block with its reward going to the mining wallet.
4. Check that the payment is actually included in that block. Do not assume inclusion just because you generated one.
5. Query the same transaction, relevant outputs, and mempool again. Compare them with the previous observation.
6. Generate another block and repeat. Explain the confirmation count using the observed heights.
7. Implement a way to collect and compare these observations in Python without hard-coding the values you expect to see.

If the payment is not included, the experiment is still useful: investigate its mempool presence, validity, fee rate, and possible dependencies before blindly repeating it.

## Interpreting the results

Each node has its own mempool; this lab observes one node's view. There is no single global queue with an identical state for everyone.

A wallet can show pending funds or treat its own change differently from a received payment. Confirmation, visibility, and spendability are not synonyms. State which query and filters you used.

Confirmation alone does not change the observed transaction's bytes. It adds context about its inclusion in the chain. A reorganization could change that inclusion; we'll explore this with multiple nodes in session 8.

## A variation

Shut down the node cleanly, restart it with the same data, and query the confirmed payment. First predict what should be preserved. If a wallet query fails, distinguish an unloaded wallet from lost data.

## Completion check

- You have three actual observations of the same payment: pending, included in a block, and after one more block.
- You can show the block containing the payment and explain how you counted its confirmations.
- You can explain why seeing a payment, finding it in a mempool, and confirming it are different observations.
- Your explanation does not depend on every total balance changing in a particular way.
- You can query the result again after restarting the node.

Save the code and a [note](session-template.md). Update [progress](progress.md) with what you ran and explained. Questions about conflicts or reorganizations will help shape the next sessions.

<details>
<summary>Troubleshooting hints</summary>

- Look for mempool, block, and wallet operations in `help`. Compare their scope before choosing one.
- Some mempool queries return an error if the transaction is no longer there. Absence alone does not prove confirmation: check the block.
- Accepting a pending transaction and selecting it for a block are different operations.
- If Alice's total rises while you track an outgoing payment, check whether an older reward has matured. That does not invalidate the transaction's accounting.
- For a transaction confirmed in the active chain, a known inclusion height lets you derive its confirmation count from the current height. Check the first-block case before generalizing the formula.

</details>

## References

- [Bitcoin Core 30.0 RPC reference](https://bitcoincore.org/en/doc/30.0.0/): blockchain and wallet operations.
- [Confirmations and wallet context: gettransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/gettransaction/).
- [Controlling blocks in regtest](https://developer.bitcoin.org/examples/testing.html#regtest-mode).
