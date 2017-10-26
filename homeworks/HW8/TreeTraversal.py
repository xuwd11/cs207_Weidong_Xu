
from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    
class Node:
    def __init__(self, value, depth=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.depth = depth
        
    def set_left(self, left):
        self.left = left
        if left is not None:
            left.parent = self
            left.set_depth(self.depth + 1)
        
    def set_right(self, right):
        self.right = right
        if right is not None:
            right.parent = self
            right.set_depth(self.depth + 1)
        
    def set_parent(self, parent):
        self.parent = parent
        
    def set_depth(self, depth):
        self.depth = depth
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        curr = self.root
        while True:
            if curr < new_node:
                if curr.right is None:
                    curr.set_right(new_node)
                    return
                else:
                    curr = curr.right
                    continue
            elif new_node < curr:
                if curr.left is None:
                    curr.set_left(new_node)
                    return
                else:
                    curr = curr.left
                    continue
            elif new_node == curr:
                new_node.set_left(curr.left)
                curr.set_left(new_node)
                # update depth for the subtree
                self.getInOrder(new_node)
                return
    
    def remove(self, val):
        curr = self.root
        from_ = None
        while True:
            if val < curr.value:
                curr = curr.left
                from_ = 1
                if curr is None:
                    return
                continue
            elif curr.value < val:
                curr = curr.right
                from_ = 2
                if curr is None:
                    return
                continue
            else:
                if curr.left is None and curr.right is None:
                    if from_ is None:
                        self.root = None
                    elif 1 == from_:
                        curr.parent.set_left(None)
                    else:
                        curr.parent.set_right(None)
                elif curr.left is not None and curr.right is None:
                    if from_ is None:
                        self.root = curr.left
                        self.root.set_parent(None)
                        self.root.set_depth(0)
                        # update depth for the subtree
                        self.getInOrder(self.root)
                    elif 1 == from_:
                        curr.parent.set_left(curr.left)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                    else:
                        curr.parent.set_right(curr.left)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                elif curr.left is None and curr.right is not None:
                    if from_ is None:
                        self.root = curr.right
                        self.root.set_parent(None)
                        self.root.set_depth(0)
                        # update depth for the subtree
                        self.getInOrder(self.root)
                    elif 1 == from_:
                        curr.parent.set_left(curr.right)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                    else:
                        curr.parent.set_right(curr.right)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                else:
                    # find the node (`r_node`) with the maximum value in the left subtree
                    r_node = curr.left
                    if r_node.right is None:
                        is_left = True
                    else:
                        is_left = False
                    while r_node.right is not None:
                        r_node = r_node.right
                    if is_left:
                        r_node.set_right(curr.right)
                    else:
                        r_node.parent.set_right(r_node.left)
                        r_node.set_left(curr.left)
                        r_node.set_right(curr.right)
                    if from_ is None:
                        self.root = r_node
                        self.root.set_parent(None)
                        self.root.set_depth(0)
                        # update depth for the subtree
                        self.getInOrder(self.root)
                    elif 1 == from_:
                        curr.parent.set_left(r_node)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                    else:
                        curr.parent.set_right(r_node)
                        # update depth for the subtree
                        self.getInOrder(curr.parent)
                break
        self.remove(val)
                            
    def getValues(self, depth):
        inorder = self.getInOrder(self.root)
        values = []
        for node in inorder:
            if node.depth > depth:
                continue
            elif node.depth == depth:
                values.append(node.value)
            else:
                if node.left is None:
                    values += [None] * 2**(depth-node.depth-1)
                if node.right is None:
                    values += [None] * 2**(depth-node.depth-1)
        return values
    
    def getInOrder(self, node):
        # in-order traversal
        # update depth
        inorder = []
        def _inorder(node, inorder):
            if node is None:
                return
            elif node.parent is not None:
                node.set_depth(node.parent.depth + 1)
            _inorder(node.left, inorder)
            inorder.append(node)
            _inorder(node.right, inorder)
        _inorder(node, inorder)
        return inorder
    
    def maxDepth(self):
        inorder = self.getInOrder(self.root)
        return max([i.depth for i in inorder])
    
    def __len__(self):
        return self.maxDepth() + 1
    
class DFSTraversal:
    def __init__(self, tree, traversalType):
        self.tree = tree
        self.traversalType = traversalType
        self.changeTraversalType(traversalType)
    
    def changeTraversalType(self, traversalType):
        if not traversalType in DFSTraversalTypes:
            raise TypeError('Invalid traversalType')
        self.traversalType = traversalType
        if traversalType == DFSTraversalTypes.PREORDER:
            self.traversal = self.getPreOrder(self.tree.root)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.traversal = self.getInOrder(self.tree.root)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.traversal = self.getPostOrder(self.tree.root)
    
    def getPreOrder(self, node):
        traversal = []
        if node is None:
            return traversal
        s = []
        s.append(node)
        while len(s) > 0:
            node = s.pop()
            traversal.append(node.value)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
        return traversal
    
    def getInOrder(self, node):
        traversal = []
        s = []
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                traversal.append(node.value)
                node = node.right
        return traversal
    
    def getPostOrder(self, node):
        traversal = []
        s = []
        last_node_visited = None
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                peek_node = s[-1]
                if peek_node.right is not None and id(last_node_visited) != id(peek_node.right):
                    node = peek_node.right
                else:
                    traversal.append(peek_node.value)
                    last_node_visited = s.pop()
        return traversal
    
    def __getitem__(self, i):
        return self.traversal[i]
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        try:
            elem = self.traversal[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return elem