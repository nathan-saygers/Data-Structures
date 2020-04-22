import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # variable for number of held nodes
        self.limit = limit
        # doubly linked list that holds key value entries
        self.storage = DoublyLinkedList()
        # dictionary that holds a key, then values of the linked list in the same order
        self.map = {}
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.map:
            # Move key:value to end of order
            node = self.map[key]
            self.storage.move_to_end(node)
            # Return the value associated with the key passed
            return node.value[1]
        else:
            # or none if doesn't exist
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # IF the key already exists
        if key in self.map:
            # Update the value THIS NEEDS TO UPDATE THE NODE IN STORAGE
            node = self.map[key]
            node.value = (key, value)
            # Move the node to the end of the list
            self.storage.move_to_end(node)
            return
        # If the length of storage is equal to the limit:
        if self.storage.length == self.limit:
            # Remove the head of storage
            old_node = self.storage.head.value[0]
            del self.map[old_node]
            #remove the head node from DLL
            self.storage.remove_from_head()
            self.size -= 1
        # key is not in storage and we still have room in cache
        # add the key / value
        self.storage.add_to_tail((key, value))
        self.map[key] = self.storage.tail
        self.size += 1
          