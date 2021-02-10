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
# by postorder (left, right, root)
def postorder_recursion(root):
	'''
	function name: postorder_recursion
	parameters: tree.root, read in a binary tree's root
	return: string, the postorder of this binary tree
	'''
	if not root:
		return ''
	if root.value and not root.left and not root.right:
		return str(root.value)+" - "
	traversal = ''
	traversal += postorder_recursion(root.left)
	traversal += postorder_recursion(root.right)
	traversal += str(root.value)+" - "
	return traversal

print(postorder_recursion(tree.root))















