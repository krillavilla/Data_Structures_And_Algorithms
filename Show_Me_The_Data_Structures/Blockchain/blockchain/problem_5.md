# Explanation for Problem 5: Blockchain Implementation

In this problem, I'm implementing a simple blockchain using a linked list. Each block in the blockchain contains a timestamp, some data, a cryptographic hash of the previous block, and a reference to the next block.

## Block Class

The `Block` class represents a block in the blockchain. It has the following attributes:

- `timestamp`: The time when the block was created.
- `data`: The data stored in the block.
- `previous_hash`: The cryptographic hash of the previous block.
- `hash`: The cryptographic hash of the current block.
- `next`: A reference to the next block in the chain.

The `Block` class also has a method `calc_hash` that calculates the cryptographic hash of the block's data using the SHA-256 algorithm.

## Test Cases

I have also included some test cases to validate our blockchain implementation. These test cases add blocks with different types of data (normal data, empty data, and very large data) to the blockchain and then validate the chain. The expected result for all test cases is `True`, indicating that the blockchain is valid.

## Reasoning and Efficiency

The decision to use a linked list for the blockchain implementation is due to the inherent characteristics of a blockchain where each block is linked to its previous block, similar to how each node in a linked list points to its previous node. This makes the linked list a suitable data structure for this implementation.

The time efficiency of adding a block is O(1) because we always add the new block at the head of the chain. The time efficiency of validating the chain is O(n) because we need to traverse the entire chain. The space efficiency of our solution is also O(n) because we need to store all the blocks in the chain.