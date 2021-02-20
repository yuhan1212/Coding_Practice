# Construct Node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Construct BinaryTree class        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

# Instanciate a tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#               1
#           /       \  
#          2          3  
#         / \        / \
#        4    5     6   7 
#       /      \   /     \
#      N        N  N      N
 

# Read and process each data in the Node of a BinaryTree,
# by levelorder.
def levelorder_recursion(root):
    '''
    function name: levelorder_recursion
    parameters: root, read in a binary tree's root
    return: string, the postorder of this binary tree
    '''
    if not root:
        return ""
    current_level = [root]
    next_level = []
    traversal = ""
    for i in current_level:
        traversal += str(i.value) + " - "
        if i.left:
            next_level += [i.left]
        if i.right:
            next_level += [i.right]

    while next_level != []:
        current_level = next_level
        next_level = []
        for i in current_level:
            traversal += str(i.value) + " - "
            if i.left:
                next_level += [i.left]
            if i.right:
                next_level += [i.right]
    return traversal

print(levelorder_recursion(tree.root))