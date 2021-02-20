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



#               1  
#           /       \  
#          2         3  
#         /  \      /  \
#        N    N    N    N


	def inorder(self, start, traversal): 
						# statr=Node(1), traversal=""

	    if start: # statr=Node(1)


	        traversal = self.inorder_print(start.left, traversal) 
	        								# Node(1)'s left
	          
	          
	                    def inorder_print(self, start, traversal): 	
	                    					# statr=Node(1)'s left=Node(2), traversal=""
	                        
	                        if start: # start=Node(2) 

	                            traversal = self.inorder_print(start.left, traversal) 	
	                            								# statr=Node(2)'s left, traversal=""
	                      
	                        				def inorder_print(self, start, traversal): 
	                        									# statr=Node(2)'s left=None, traversal=""
	                          								
	                                            if start:  # start=None 

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.inorder_print(start.left, traversal)
	                                                traversal = self.inorder_print(start.right, traversal)

	                                            return traversal # traversal = ""
	                            
	                            traversal += (str(start.value) + "-") #  "2-"

								traversal = self.inorder_print(start.right, traversal)  
	                            								# statr=Node(2)'s right=None, traversal="2-"

	                            			def inorder_print(self, start, traversal):

	                                            if start: # start=None 

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.inorder_print(start.left, traversal)
	                                                traversal = self.inorder_print(start.right, traversal)

	                                            return traversal # traversal = "2-"
	                           
	                          return traversal # traversal = "2-"     

	        traversal += (str(start.value) + "-")  # "2-1-"
	        
	        
	        traversal = self.inorder_print(start.right, traversal)
	        								# Node(1)'s right 

	        			def inorder_print(self, start, traversal):
	        								# statr=Node(1)'s right=Node(3), traversal="2-1-"

	                        if start: # stsrt=Node(3)

	                            traversal = self.inorder_print(start.left, traversal)
	                        									# statr=Node(3)'s left=None, traversal="2-1-"

	                        				def inorder_print(self, start, traversal):

	                                            if start: # start=None

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.inorder_print(start.left, traversal)
	                                                traversal = self.inorder_print(start.right, traversal)

	                                            return traversal # traversal = "2-1-"

	                        	traversal += (str(start.value) + "-") # traversal = "2-1-3-"


	                            traversal = self.inorder_print(start.right, traversal)
	                            								# statr=Node(3)'s right=None, traversal="2-1-3-"

	                                        def inorder_print(self, start, traversal):

	                                            if start: # start=None

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.inorder_print(start.left, traversal)
	                                                traversal = self.inorder_print(start.right, traversal)

	                                            return traversal # traversal = "2-1-3-"
	                            
	                        return traversal # traversal = "2-1-3-"
	        			
	    return traversal # traversal = "2-1-3-"
















