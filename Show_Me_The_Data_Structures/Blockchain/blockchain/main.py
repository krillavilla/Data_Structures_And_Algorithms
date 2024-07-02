# Import necessary libraries
import hashlib
import datetime

# Define the Block class
class Block:
    def __init__(self, data, previous_hash):
        # Initialize block with current timestamp, data, previous hash, and calculate its own hash
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Create a new SHA256 hash object
        sha = hashlib.sha256()
        # Create a string that contains the data, timestamp and previous hash
        hash_str = str(self.data).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(
            self.previous_hash).encode('utf-8')
        # Update the hash object with the above string
        sha.update(hash_str)
        # Return the hexadecimal representation of the hash
        return sha.hexdigest()

    def __str__(self):
        # Define the string representation of the block
        return (f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"SHA256 Hash: {self.hash}\n"
                f"Previous Hash: {self.previous_hash}\n"
                "--------------------------------------")

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        # Initialize blockchain with a genesis block
        genesis_data = "Chancellor on Brink of Second Bailout for Banks"
        genesis_block = Block(genesis_data, None)
        self.current_block = genesis_block
        # Initialize a hash table to store blocks
        self.hash_table = {}
        self.hash_table[genesis_block.hash] = genesis_block

    def add_block(self, block):
        # Add a new block to the blockchain
        block.previous_hash = self.current_block.hash
        self.current_block = block
        self.hash_table[block.hash] = block

    def get_current_block(self):
        # Get the current block in the blockchain
        return self.current_block

    def hash_table_lookup(self, hash):
        # Lookup a block in the hash table by its hash
        return self.hash_table[hash]

# Create the blockchain
blockchain = Blockchain()

# Create some blocks and add them to the blockchain
block1 = Block("Test block #1", blockchain.get_current_block().hash)
blockchain.add_block(block1)

block2 = Block("Test block #2", blockchain.get_current_block().hash)
blockchain.add_block(block2)

# Print out the blockchain
print(blockchain.hash_table[block1.hash])
print(blockchain.hash_table[block2.hash])

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Add a block with empty data
print("Test Case 1")
block3 = Block("", blockchain.get_current_block().hash)
blockchain.add_block(block3)
print(blockchain.hash_table[block3.hash])

# Test Case 2: Add a block with null data
print("Test Case 2")
block4 = Block(None, blockchain.get_current_block().hash)
blockchain.add_block(block4)
print(blockchain.hash_table[block4.hash])

# Test Case 3: Add a block with normal data
print("Test Case 3")
block5 = Block("Test block #3", blockchain.get_current_block().hash)
blockchain.add_block(block5)
print(blockchain.hash_table[block5.hash])