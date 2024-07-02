# Explanation for LRU Cache Implementation

The LRU Cache was implemented using a combination of a doubly linked list and a dictionary. The doubly linked list is used to keep track of the order of elements (from most recently used to least recently used), while the dictionary provides quick access to any element in the cache.

## Reasoning Behind Decisions

The decision to use a doubly linked list and a dictionary was made based on the requirements of an LRU Cache. The cache needs to have quick access to elements (O(1) time complexity), and it also needs to quickly remove and add elements. A doubly linked list allows us to remove and add elements in O(1) time, and a dictionary allows us to access elements in O(1) time.

## Time Efficiency

The time efficiency of the `get` and `set` operations in this LRU Cache implementation is O(1). This is because accessing, removing, and adding elements in a dictionary and a doubly linked list can be done in constant time.

## Space Efficiency

The space efficiency of this LRU Cache implementation is O(n), where n is the capacity of the cache. This is because we store each element in the cache in both a dictionary and a doubly linked list. The space used by the cache is proportional to the number of elements stored in it.