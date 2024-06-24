# Show Me The Data Structures

## Introduction

Welcome to the "Show Me The Data Structures" project repository. This repository contains solutions to various data structure problems implemented in Python. Each problem is designed to test your understanding and implementation skills of different data structures and algorithms commonly used in software development.

### Project Structure

The repository is structured as follows:

- **Problem Solutions**: Each problem has its own Python file named after the problem title. For example, `LRU_Cache.py` contains the solution for the LRU Cache problem.
  
- **README.md**: This file provides an overview of the project, describes each problem, their solutions, and instructions for running and testing the code.

- **Test Cases**: Each problem includes example test cases within the problem description. Additional test cases can be added by following the format provided.

## Problems

### Problem 1: LRU Cache

**Description**: Implement an LRU (Least Recently Used) cache that supports get and set operations in constant time, O(1).

**File**: `LRU_Cache.py`

**Solution**: The solution utilizes a dictionary for fast lookup and a list to maintain the order of recently used keys.

**Test Cases**: Example test cases are provided within the file. Additional test cases can be added to validate edge cases and performance.

### Problem 2: File Recursion

**Description**: Write a function to find all files under a directory (and all directories beneath it) that end with ".c".

**File**: `File_Recursion.py`

**Solution**: The solution uses recursive traversal of directories and checks file extensions using Python's `os` module.

**Test Cases**: Example test cases are provided within the file. More test cases can be added to cover different directory structures and edge cases.

### Problem 3: Huffman Coding

**Description**: Implement Huffman encoding and decoding algorithms for data compression.

**Files**: `Huffman_Encoding.py`, `Huffman_Decoding.py`

**Solution**: The encoding phase builds a Huffman tree and generates encoded data. The decoding phase uses the tree to decode the data.

**Test Cases**: Example test cases are included. Additional cases can be added to cover different input strings and scenarios.

### Problem 4: Active Directory

**Description**: Implement a function to efficiently check if a user belongs to a group in Active Directory.

**File**: `Active_Directory.py`

**Solution**: Uses a recursive search through groups and users to determine membership.

**Test Cases**: Example test cases are provided. More can be added to test different group structures and edge cases.

### Problem 5: Blockchain

**Description**: Implement a basic blockchain using linked lists and hashing.

**File**: `Blockchain.py`

**Solution**: The blockchain consists of blocks linked together where each block contains a SHA-256 hash of the previous block, a timestamp, and transaction data.

**Test Cases**: Example test cases can be added to validate the functionality of blockchain operations.

### Problem 6: Union and Intersection of Two Linked Lists

**Description**: Implement functions to find the union and intersection of two linked lists.

**File**: `Union_Intersection.py`

**Solution**: Provides functions `union` and `intersection` to compute the union and intersection of two linked lists respectively.

**Test Cases**: Example test cases are provided. Additional cases can be added to cover edge cases and large inputs.

