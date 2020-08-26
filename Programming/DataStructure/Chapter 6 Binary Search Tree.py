# Chapter 6 Binary Search Tree

# Chapter 6 - 1 Tree as an Abstract Data Type and Structure
'''
Weekly Objectives - BINARY SEARCH TREE, HEAP
    This week, we study the tree data structure. Particularly, we will focus on the structure and the operation of the binary search tree.
    Objectives are
        Memorizing the definitions, the terminologies  and the characteristics of trees
        Understanding the structures of trees
        Understanding the structure and the operations of a binary search tree / B - tree, AVL, RB
        Insert, search, delete operations
        Tree traversing operations
        Depth first search
        In-order, post-order, pre-order sequences
        Breadth first search
        Level order search
        Understanding the performance of binary search tree

'''

'''
Tree as an abstract data type
    Tree structure - Abstract data type
    Data stored - As a tree structure
    Operations- Ordinary data structure operations just as linked lists
        Insert
        Delete
        Search
    Special searching approaches for trees and networks
        Traverse - 방법이 많아.

Why do we use trees?
    Because the structure of trees is a good analogy to the various real world structures
        Corporate structures
        Group bank accounts
        Command and control structures
    Why is the structure one of the most favorite structures?
        A clear approach of Divide and Conquer
    
    Nothing but with multiple ‘next’s / NEXT가 여러개를 가질 수 있다. / LAYER 넘어갈 수록 N^LAYER-1로 노드수가 늘어남
        Each node has multiple next nodes
        Particularly, this structure maintains the next nodes as an array or variables
'''

# Chapter 6 - 2 Terminologies of Tree Structure

'''

'''

# Chapter 6 - 3 Characteristics of trees
'''

(Num. of edges) =  (Num. of nodes) – 1
Depth of root = 0
height of root = height of tree
(Maximum num. of nodes at level i with degree d) = d ^ i
(Maximum num. of leaves with height h and degree d)  = d ^ h
(Maximum size of a tree with height h and degree d) = 1+d+d^2+…+d^h= (𝑑^(ℎ+1)−1)/(𝑑−1)
(Height of a complete tree with size s and degree d) =⌈log_𝑑⁡〖(𝑠(𝑑−1)+1)〗 ⌉-1
'''

# Chapter 6 - 4 Binary search tree: a simple structure(BST)
'''
    Binary tree - Tree with degree 2
    Binary search tree
    Tree with degree 2
    Tree designed for a fast search of stored data
    So far, what we have studied the definitions and the characteristics of stored data
    Now, this is related to the operations
    How to perform a faster search?
    Do you remember what I discussed in the lecture 0?

Implementation of tree node
    Has three references
        Left hand side (LHS)
        Right hand side (RHS)
        Its own value
        Its parent node
        Not implemented here, but
        LHS stores
        Values have lower than its own value
        RHS stores
        Values have higher than its own value
        Just as we all know that the department stores do not have a restroom on the first floor
    Other than four references,
        Simple get/set methods
        What are the get/set methods?
        Coming from encapsulation

'''

from datastructure import *

class TreeNode :
    nodeLHS = ''
    nodeRHS = ''
    nodeParent = ''
    value = ''

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self) :
        return self.nodeLHS
    def getRHS(self) :
        return self.nodeRHS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent
    def setLHS(self, LHS):
        self.nodeLHS = LHS
    def setRHS(self, RHS):
        self.nodeRHS = RHS
    def setValue(self, value):
        self.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent
'''
class BinarySearchTree :
    root = ''

    def __init__(self):
        pass
    def insert(self, value, node = ''):
        pass

    def search(self, value, node = ''):
        pass

    def delete(self, value, node = ''):
        pass

    def findMax(self, node =''):
        pass

    def findMax(self, node = ''):
        pass

    def traverseLevelOrder(self):
        pass

    def traversePreOrder(self):
        pass

    def traversePostOrder(self):
        pass
'''
# Chapter 6 - 5 Insert and Search Operation of Binary Search Tree
# Chapter 6 - 6 Delete Operation and Minimum & Maximum of Binary Search Tree
'''
Insert operation of binary search tree

    Insertion operation
        Retrieve the current node value
        If the value is equal to the value to insert - Return already there! / insert하지 않음
        
        If the value is smaller than the value to insert
        If there is a node in the right hand-side (RHS), then move to the RHS node (Recursion)
        If there is no node in RHS, create a RHS node with the value to insert
        
        If the value is larger than the value to insert
        If there is a node in the left hand-side (LHS), then move to the LHS node (Recursion)
        If there is no node in LHS, create a LHS node with the value to insert

Search operation
    Retrieve the current node value
    If the value is equal to the value to search =    Return TRUE
    If the value is smaller than the value to search
        If there is a node in the right hand-side (RHS), then move to the RHS node (Recursion)
        If there is no node in RHS, return FALSE
    If the value is larger than the value to search
        If there is a node in the left hand-side (LHS), then move to the LHS node (Recursion)
        If there is no node in LHS, return FALSE

'''

'''
Delete operation of binary search tree (1)

    First, you need to find the node to delete through recursions / child 있으면 복잡해져
    Three deletion cases
        Case 1: deleting a node with no children
        Just remove the node by modifying its parent
        Case 2: deleting a node with one child
        Replace the node with the child
        Case 3: deleting a node with two children // 중간에 가까운 것을 이용 right의 minimum, left의 maximum
        Find either
        A maximum in the LHS or A minimum in the RHS
        Substitute the node to delete with the found value
        Delete the found node in the LHS or the RHS 
'''
'''
Minimum and maximum in binary search tree
Finding minimum in a BST
Just keep following the LHS
Because this will always result in the smaller value than the value of the current node
When you can’t any LHS, then the value of the current node is the smallest
Finding maximum in a BST
Just keep following the RHS
Because this will always result in the larger value than the value of the current node
When you can’t any RHS, then the value of the current node is the largest

'''

class BinarySearchTree :
    root = ''
    def __init__(self):
        pass

    def insert(self, value, node = ''):
        if node == '' :
            node = self.root
        if self.root == '' :
            self.root = TreeNode(value, '')
            return
        if value == node.getValue() :
            return

        if value > node.getValue() :
            if node.getRHS() == '' :
                node.setRHS(TreeNode(value, node))
            else:
                self.insert(value, node.getRHS())

        if value < node.getValue() :
            if node.getLHS() == '' :
                node.setLHS(TreeNode(value, node))
            else :
                self.insert(value, node.getLHS())
        return
    def search(self, value, node = ''):
        if node == '' :
            node = self.root
        if value == node.getValue(): # escape route
            return True
        if value > node.getValue() :
            if node.getRHS() == '' :
                return False
            else :
                return self.search(value, node.getRHS())
        if value < node.getValue() :
            if node.getLHS() == '' :
                return False
            else :
                return self.search(value, node.getLHS())

    def delete(self, value, node = ''):
        if node == '' :
            node = self.root
        if node.getValue() < value :
            return self.delete(value, node.getLHS())
        if node.getValue() > value :
            return self.delete(value, node.getRHS())
        if node.getValue() == value :
            if node.getLHS() != '' and node.getRHS() != '' :
                nodeMIn = self.findMin(node.getRHS())
                node.setValue(nodeMIn.getValue())
                self.delete(nodeMIn.getValue(), node.getRHS())
                return
            parent = node.getParent()
            if node.getLHS() != '' : # one child with left
                if node == self.root : # node가 root면 lhs를 root로 가져와라
                    self.root = node.getLHS()
                elif parent.getLHS() == node : # node의 parent의 left가 node일 경우 parent의 node의 lhs를 옮겨온다
                    parent.getLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else : # node의 parent의 right가 node일 경우 parent의 reight의 node의 lhs를 가져온다.
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node.getRHS() != '' :
                if node == self.root :
                    self.root = node.getRHS()
                elif parent.getRHS() == node :
                    parent.getRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else :
                    parent.getLHS(node.getLHS())
                    node.getRHS().setParent(parent)
                return
            if node == self.root :
                self.root = ''
            elif parent.getLHS() == node :
                parent.setLHS('')
            else :
                parent.setRHS('')
            return

    def findMax(self, node =''):
        if node == '' :
            node = self.root
        if node.getRHS() == '' :
            return node
        return self.findMax(node.getRHS())

    def findMin(self, node = ''):
        if node == '' :
            node = self.root
        if node.getLHS() == '' :
            return node
        return self.findMin(node.getLHS())

    def traverseInorder(self, node = ''):
        if node == '' :
            node = self.root

        ret = []
        if node.getLHS() != '' :
            ret = ret + self.traverseInorder(node.getLHS())
        ret.append(node.getValue())
        if node.getRHS() != '' :
            ret = ret + self.traverseInorder(node.getRHS())
        return ret

    def traversePreOrder(self, node = ''):
        if node == '':
            node = self.root

        ret = []
        ret.append(node.getValue())
        if node.getLHS() != '':
            ret = ret + self.traversePreOrder(node.getLHS())

        if node.getRHS() != '':
            ret = ret + self.traversePreOrder(node.getRHS())
        return ret

    def traversePostOrder(self, node = ''):
        if node == '':
            node = self.root

        ret = []
        if node.getLHS() != '':
            ret = ret + self.traverseInorder(node.getLHS())

        if node.getRHS() != '':
            ret = ret + self.traverseInorder(node.getRHS())
        ret.append(node.getValue())
        return ret

    def traverseLevelOrder(self):
        ret = []
        Q = Queue()
        Q.Enqueue(self.root)
        while Q.isEmpty() == False :
            node = Q.Dequeue()
            if node == '' :
                continue
            ret.append(node.getValue())
            if node.getLHS() != '' :
                Q.Enqueue(node.getLHS())
            if node.getRHS() != '' :
                Q.Enqueue(node.getRHS())
        return  ret

Q2 = Queue()
Q2.isEmpty()
tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(0)
tree.insert(5)
tree.insert(7)
tree.insert(4)
tree.insert(6)
tree.insert(1)
tree.insert(9)
tree.insert(8)
tree.search(4)
print(tree.traversePreOrder())
print(tree.traverseInorder())
print(tree.traversePostOrder())
print(tree.traverseLevelOrder())

tree.delete(5)
print(tree.traversePostOrder())
# Chapter 6- 6 Tree traversing
'''
Tree
    Complicated than a list
    Multiple ways to show the entire dataset
        If it were a list
        Just show the values from the beginning to the end
        Since this is a BST
        You have to choose what to show at a time
        The value in LHS
        The value in RHS
        The value that you have
    Hence there are multiple traversing approaches

Depth first traverse
    Pre-order traverse
    Order: Current, LHS, RHS in Recursion
    3, 2, 0, 1, 5, 4, 7, 6, 9, 8
    In-order traverse / it's same sorting
    Order: LHS, Current, RHS in Recursion
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Post-order traverse
    Order: LHS, RHS, Current in Recursion
    1, 0, 2, 4, 6, 8, 9, 7, 5, 3
   
Breadth first traverse
    Queue-based level-order traverse
    3, 2, 5, 0, 4, 7, 1, 6, 9, 8
    Enqueue the root
        While until queue is empty
        Current = Dequeue one element
        Print current
        If Current’s LHS exist
        Enqueue current.LHS
        If Current’s RHS exist
        Enqueue current.RHS
     
'''


