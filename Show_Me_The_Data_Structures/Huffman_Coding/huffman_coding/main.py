
# Import the required libraries
import heapq
import sys
from collections import defaultdict

# Define Node class to represent a node in the Huffman tree
class Node:
    # Constructor to initialize the node
    def __init__(self, char, freq):
        self.char = char # character stored in the node
        self.freq = freq # frequency of the character
        self.left = None # left child of the node
        self.right = None # right child of the node

    # Define less than function for the node
    def __lt__(self, other):
        return self.freq < other.freq # compare nodes based on their frequency

# Define helper functions to build the Huffman tree
def calculate_frequency(data):
    # Calculate the frequency of each character in the data
    frequency = defaultdict(int)
    # Iterate over each character in the data
    for char in data:
        # Increment the frequency of the character
        frequency[char] += 1
    # Return the frequency dictionary
    return frequency

# Define helper functions to build the Huffman tree
def build_huffman_tree(frequency):
    # Create a priority queue to store the nodes
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    # Convert the list into a heap
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        # Pop out the two nodes with the lowest frequency
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        # Create a new node with the sum of frequencies
        merged_node = Node(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        # Insert the new node back into the priority queue
        heapq.heappush(priority_queue, merged_node)

    return heapq.heappop(priority_queue)

# Define helper functions to build the Huffman codes
def build_codes_helper(root, current_code, codes):
    if root is None: # base case
        return # return if the root is None

# Define helper functions to build the Huffman codes
    if root.char is not None:
        # Assign the code to the character
        codes[root.char] = current_code

    # Traverse the left subtree with code '0'
    build_codes_helper(root.left, current_code + "0", codes)
    # Traverse the right subtree with code '1'
    build_codes_helper(root.right, current_code + "1", codes)

# Define helper functions to build the Huffman codes
def build_codes(root):
    codes = {} # dictionary to store the codes
    build_codes_helper(root, "", codes) # build the codes
    return codes

# Define the main functions for encoding and decoding
def huffman_encoding(data):
    if not data:
        return "", None

    frequency = calculate_frequency(data) # calculate the frequency
    huffman_tree = build_huffman_tree(frequency) # build the Huffman tree
    codes = build_codes(huffman_tree) # build the Huffman codes

    encoded_data = "".join([codes[char] for char in data]) # encode the data

    return encoded_data, huffman_tree

# Define the main functions for encoding and decoding
def huffman_decoding(data, tree):
    decoded_data = "" # initialize the decoded data
    current_node = tree # start from the root of the tree

    # Traverse the encoded data
    for bit in data:
        # Move to the left child if the bit is '0'
        if bit == '0':
            current_node = current_node.left
        # Move to the right child if the bit is '1'
        else:
            # Move to the right child
            current_node = current_node.right

# Define the main functions for encoding and decoding
        if current_node.char is not None:
            # Append the character to the decoded data
            decoded_data += current_node.char
            # Move back to the root of the tree
            current_node = tree

    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
sentence1 = "The bird is the word"
encoded_data1, tree1 = huffman_encoding(sentence1)
decoded_data1 = huffman_decoding(encoded_data1, tree1)
assert sentence1 == decoded_data1, "Test Case 1 Failed"

## Test Case 2
sentence2 = ""
encoded_data2, tree2 = huffman_encoding(sentence2)
decoded_data2 = huffman_decoding(encoded_data2, tree2) if tree2 else ""
assert sentence2 == decoded_data2, "Test Case 2 Failed"

## Test Case 3
sentence3 = "a" * 10000 + "b" * 10000 + "c" * 10000  # large frequencies
encoded_data3, tree3 = huffman_encoding(sentence3)
decoded_data3 = huffman_decoding(encoded_data3, tree3)
assert sentence3 == decoded_data3, "Test Case 3 Failed"

print("All test cases passed!")