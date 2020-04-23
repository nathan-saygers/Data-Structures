import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTreeNode:
    # Note about class name: it's more of a BST NODE than a tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty (can park)
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        # otherwise value is >= self.value
        else:
            if self.right:
                self.right.insert(value)
            # if no right hand value
            else:
                self.right = BinarySearchTreeNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if value is target
        if target == self.value:
            return True
        # self.left and/or self.right need to be valid nodes
        # for us to call contains on them
        if target < self.value:
            # check if self.left is a valid node
            if self.left:
                return self.left.contains(target)
            else:
                return False
        # otherwise target is >= self.value
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check if the current node has a self.right
        if self.right:
            # if yes: call get_max again
            return self.right.get_max()
        # if no: return self.value
        else:
            return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Use the callback on the self.value of the current node
        self.value = cb(self.value)
        # Check to see if there is a self.left
        if self.left:
            # Call again on self.left
            self.left.for_each(cb)
        # Check to see if there is a self.right
        if self.right:
            # Call again on self.right
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack 
        stack.append(self)
        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack 
        # breadth-first : queue
        # q = Queue()
        # q.enqueu(self)
        # while len(q) > 0:
        #     current_node = q.popleft()
        #     if current_node.left:
        #         q.enqueu(current_node.left)
        #     if current_node.right:
        #         q.enqueu(current_node.right)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # IF there is a left node, call again on left node
        if node.left:
            node.in_order_print(node.left)
        # Print node
        print(node.value)
        # IF there is a node to the right, call again on right
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        store = Queue()
        store.enqueue(node)
        # Put current node into the store
        while store.size > 0:
            current_node = store.dequeue()
            if current_node.left:
                store.enqueue(current_node.left)
            if current_node.right:
                store.enqueue(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        # add the root of the tree to the stack 
        stack.append(self)
        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# tester = BinarySearchTreeNode(10)
# tester.insert(3)
# tester.insert(1)
# tester.insert(15)
# tester.insert(8)
# tester.insert(20)
# tester.insert(25)

# def add1(val):
#     print(val)

# tester.dft_print(tester)
# print(tester.left.value)
# print(tester.right.value)