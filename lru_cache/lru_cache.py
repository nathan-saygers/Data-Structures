import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

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

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.map.keys():
            print('key from inside GET', key)
            # Move key:value to end of order
            self.storage.move_to_end(self.map[key])
            print('self.map[key]:', self.map[key])
            # Return the value associated with the key passed
            return self.map[key]
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
        if key in self.map.keys():
            # Update the value THIS NEEDS TO UPDATE THE NODE IN STORAGE
            self.map[key] = value
            # Move the node to the end of the list
            self.storage.move_to_end(self.map[key])
        # else: (IF the key is new)
        else:
            # If the length of storage is equal to the limit:
            if self.storage.length >= self.limit:
                # Add the new key / value to the map
                self.map[key] = value
                # Add the new value to the tail of storage
                self.storage.add_to_tail(self.map[key])
                # Remove the head of storage
                self.storage.remove_from_head()
            # If length of storage is less than limit:
            else:
                # Add the new key / value to the map
                self.map[key] = value
                # Add the new value to the tail of storage
                self.storage.add_to_tail(self.map[key])

tester = LRUCache()
tester.set('item1', 'pahoyhoy')
tester.set('item2', 'is')
tester.set('item3', 'the')
tester.set('item4', 'best')

print(tester.storage)

# test_dict = {'hi': 'there'}

# print(test_dict['jim'])