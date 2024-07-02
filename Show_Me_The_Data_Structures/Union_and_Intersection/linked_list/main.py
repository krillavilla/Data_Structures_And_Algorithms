"""
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:



"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here

    # Create a new linked list
    union_list = LinkedList()

    # Traverse the first linked list and append each element to the new linked list
    node = llist_1.head
    while node:
        union_list.append(node.value)
        node = node.next

    # Traverse the second linked list and append each element to the new linked list if it's not already present
    node = llist_2.head
    while node:
        current_node = union_list.head
        while current_node:
            if current_node.value == node.value:
                break
            current_node = current_node.next
        else:
            union_list.append(node.value)
        node = node.next

    return union_list
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here

    # Create a new linked list
    intersection_list = LinkedList()

    # Traverse the first linked list
    node = llist_1.head
    while node:
        # For each element in the first linked list, check if it's present in the second linked list
        current_node = llist_2.head
        while current_node:
            if current_node.value == node.value:
                # If it is, append it to the new linked list
                intersection_list.append(node.value)
                break
            current_node = current_node.next
        node = node.next

    return intersection_list
    pass

## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Testing with empty linked lists

# Edge Case 1: Both linked lists are empty
linked_list_5 = LinkedList()
# Edge Case 2: One linked list is empty
linked_list_6 = LinkedList()

print (union(linked_list_5, linked_list_6))  # Expected output: ""
print (intersection(linked_list_5, linked_list_6))  # Expected output: ""

# Test Case 2: Testing with one empty linked list and one non-empty linked list

# Edge Case 1: One linked list is empty
linked_list_7 = LinkedList()

# Edge Case 2: Both linked lists are non-empty
linked_list_8 = LinkedList()

# Adding elements to the linked list
element = [1, 2, 3, 4, 5]
# Adding elements to the linked list
for i in element:
    # Adding elements to the linked list
    linked_list_8.append(i)

print (union(linked_list_7, linked_list_8))  # Expected output: "1 -> 2 -> 3 -> 4 -> 5 -> "
print (intersection(linked_list_7, linked_list_8))  # Expected output: ""

# Test Case 3: Testing with very large values

# Edge Case 1: Very large values
linked_list_9 = LinkedList()
# Edge Case 2: Very large values
linked_list_10 = LinkedList()

# Adding elements to the linked list
element_1 = [10**18, 10**19, 10**20]
# Adding elements to the linked list
element_2 = [10**18, 10**21, 10**22]

# Adding elements to the linked list
for i in element_1:
    # Adding elements to the linked list
    linked_list_9.append(i)

# Adding elements to the linked list
for i in element_2:
    # Adding elements to the linked list
    linked_list_10.append(i)

# Expected output: "1000000000000000000 -> 100000000000000000000 -> 1000000000000000000000 -> 100
print (union(linked_list_9, linked_list_10))

# Expected output: "1000000000000000000 -> "
print (intersection(linked_list_9, linked_list_10))