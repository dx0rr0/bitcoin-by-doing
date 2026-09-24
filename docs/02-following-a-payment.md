# Session 2 · Following a payment from start to finish

[Previous: session 1](01-where-are-the-bitcoins.md) · [Course outline](README.md) · [Next: session 3](03-from-pending-to-confirmed.md)

**Question:** when Alice pays Bob, what gets consumed, what gets created, and where does the fee go?

**Starting point:** Alice has mature funds in the lab from session 1. Bob is another local wallet. Check the network, height, and funds before starting; remembering the previous state is not enough.

**What you'll build:** a Python-based explanation of one specific transaction. It must trace back to the previous outputs being spent. You choose how to query it, organize the code, and show the result.

## Predict before sending

- If Alice uses an output worth more than the payment, what do you expect to happen to the difference?
- Do you think there is an output called “fee”?
- Do you expect Bob to see anything before a block is generated?

## Guided experiment

1. Record Alice's outputs and both wallets' balance categories.
2. Get a Bob address and choose a payment below the available funds, leaving room for the fee. Do not send the entire balance.
3. Make one payment using the node's tools. Understand which decisions the wallet makes for you. If it needs an explicit fee rate, check the unit and set one for this lab.
4. Save the actual transaction ID and inspect the decoded transaction. **Do not generate blocks yet:** session 3 will continue with this pending payment.
5. For each input, find the previous transaction and the exact output being consumed. Read its amount from that data.
6. Inspect the new outputs. Identify those recognized by Alice and Bob using their wallets, without assuming the first is the payment or the last is change.
7. Calculate the fee from the input and output amounts. Cross-check against the sending wallet's reported value, accounting for its sign.
8. Repeat the inspection from your Python code and explain the flow with your own table or drawing.

You don't need to manually construct or sign the transaction yet. For now, observe what the wallet did; later, we'll make some of those decisions ourselves.

## What should become clear

An input identifies a previous output: it does not necessarily include the amount you need to calculate the fee. That is why you trace the previous data.

Change is a new output, not a remainder kept inside the spent output. In our lab, we can query the wallets to identify it; in someone else's transaction, you cannot always tell who controls each output.

The accounting check for this exercise is:

> Sum of the previous output amounts consumed = sum of the new outputs + fee.

We are working with an ordinary transaction. The coinbase is handled differently and is not an example to which this equality applies in the same way.

## A variation without spending more

- Query the same transaction from Alice and Bob: why might their wallet data differ even though the transaction is the same?
- Change the order in which your program presents the outputs. Does it still correctly identify their known recipients?

You don't need another payment to complete the session. First, preserve and understand this case.

## Completion check

- You can point to the previous output for every input and show where you obtained its amount.
- The amounts balance exactly, using consistent units. You did not use the wallet's fee field as your only calculation.
- You can explain what the wallet automated and what you verified yourself.
- You distinguish an observed output from an attribution about who controls it.

Save the code, an excerpt of the public test data, and a [note](session-template.md) with the payment ID, height, and observed state. Do not save wallet files. Keep the payment pending for session 3.

<details>
<summary>Troubleshooting hints</summary>

- A new regtest node may lack history for fee estimation. Check `help sendtoaddress`: an explicit rate avoids relying on that estimate. Do not confuse sat/vB with BTC/kvB.
- `gettransaction` describes a transaction from a wallet's perspective and can provide its decoded representation. For a send, the `fee` field is negative; your input-minus-output calculation expresses a positive cost.
- Keeping the funding transactions makes it easier to retrieve previous outputs. Wallet queries work for our transactions; `getrawtransaction` is not guaranteed to find any historical transaction without an index or a specified block. You don't need to index the whole chain for this exercise.
- Do not treat an output disappearing from `listunspent` as the sole proof that the payment is confirmed. We'll investigate that in the next session.

</details>

## References

- [Wallet transaction data: gettransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/gettransaction/).
- [Decoded structure: decoderawtransaction](https://bitcoincore.org/en/doc/30.0.0/rpc/rawtransactions/decoderawtransaction/).
- [Sending and parameters: sendtoaddress](https://bitcoincore.org/en/doc/30.0.0/rpc/wallet/sendtoaddress/).

Use the installed help for exact parameters. These references are for Core 30.0.
