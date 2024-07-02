# Description: Huffman Coding
class Node:
    def __init__(self, key, value):
        self.key = key # key is the key of the dictionary
        self.value = value # value is the value of the dictionary
        self.prev = None # previous node
        self.next = None # next node


# LRU Cache implementation
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        pass
# Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict: # check if the key is in the dictionary
            n = self.dict[key] # get the key from the dictionary
            self._remove(n) # remove the key from the dictionary
            self._add(n) # add the key to the dictionary
            return n.value # return the value of the key
        return -1 # return -1 if the key is not in the dictionary
        pass

# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dict: # check if the key is in the dictionary
            self._remove(self.dict[key]) # remove the key from the dictionary
        n = Node(key, value) # create a new node
        self._add(n) # add the new node to the dictionary
        self.dict[key] = n # add the key to the dictionary
        if len(self.dict) > self.capacity: # check if the length of the dictionary is greater than the capacity
            n = self.head.next # get the next node
            self._remove(n) # remove the node
            del self.dict[n.key] # delete the key from the dictionary
        pass

# Helper function to remove node from the linked list
    def _remove(self, node):
        p = node.prev # get the previous node
        n = node.next # get the next node
        p.next = n # set the next node
        n.prev = p # set the previous node
        pass

# Helper function to add node to the linked list
    def _add(self, node):
        p = self.tail.prev # get the previous node
        p.next = node # set the next node
        self.tail.prev = node # set the previous node
        node.prev = p # set the previous node
        node.next = self.tail # set the next node
        pass



our_cache = LRU_Cache(5) # create a new cache with capacity 5

our_cache.set(1, 1); # set key 1 with value 1
our_cache.set(2, 2); # set key 2 with value 2
our_cache.set(3, 3); # set key 3 with value 3
our_cache.set(4, 4); # set key 4 with value 4

our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) # set key 5 with value 5
our_cache.set(6, 6) # set key 6 with value 6

our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
our_cache = LRU_Cache(2) # create a new cache with capacity 2
our_cache.set(1, 1) # set key 1 with value 1
our_cache.set(2, 2) # set key 2 with value 2
assert our_cache.get(1) == 1 # check if the value of key 1 is 1
assert our_cache.get(2) == 2 # check if the value of key 2 is 2

## Test Case 2
our_cache = LRU_Cache(2) # create a new cache with capacity 2
our_cache.set(None, 1) # set key None with value 1
our_cache.set("", 2) # set key "" with value 2
assert our_cache.get(None) == 1 # check if the value of key None is 1
assert our_cache.get("") == 2 # check if the value of key "" is 2

## Test Case 3
our_cache = LRU_Cache(2) # create a new cache with capacity 2
our_cache.set(1, 10 ** 6) # set key 1 with value 10 ** 6
our_cache.set(2, 10 ** 6) # set key 2 with value 10 ** 6
assert our_cache.get(1) == 10 ** 6 # check if the value of key 1 is 10 ** 6
assert our_cache.get(2) == 10 ** 6 # check if the value of key 2 is 10 ** 6
