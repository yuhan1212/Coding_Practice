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


	def preorder(self, start, traversal): 
						# statr=Node(1), traversal=""

	    if start: # statr=Node(1)

	        traversal += (str(start.value) + "-")  # "1-"

	        traversal = self.preorder_print(start.left, traversal) 
	        								# Node(1)'s left
	          
	          
	                    def preorder_print(self, start, traversal): 	
	                    					# statr=Node(1)'s left=Node(2), traversal="1-"
	                        
	                        if start: # start=Node(2) 

	                            traversal += (str(start.value) + "-") #  "1-2-"

	                            traversal = self.preorder_print(start.left, traversal) 	
	                            								# statr=Node(2)'s left, traversal="1-2-"
	                      
	                        				def preorder_print(self, start, traversal): 
	                        									# statr=Node(2)'s left=None, traversal="1-2-"
	                          								
	                                            if start:  # start=None 

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.preorder_print(start.left, traversal)
	                                                traversal = self.preorder_print(start.right, traversal)

	                                            return traversal # traversal = "1-2-"
	                                      
								traversal = self.preorder_print(start.right, traversal)  
	                            								# statr=Node(2)'s right=None, traversal="1-2-"

	                            			def preorder_print(self, start, traversal):

	                                            if start: # start=None 

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.preorder_print(start.left, traversal)
	                                                traversal = self.preorder_print(start.right, traversal)

	                                            return traversal # traversal = "1-2-"
	                           
	                          return traversal # traversal = "1-2-"     
	        
	        
	        traversal = self.preorder_print(start.right, traversal)
	        								# Node(1)'s right 

	        			def preorder_print(self, start, traversal):
	        								# statr=Node(1)'s right=Node(3), traversal="1-2-"

	                        if start: # stsrt=Node(3)

	                            traversal += (str(start.value) + "-") # traversal = "1-2-3-"

	                            traversal = self.preorder_print(start.left, traversal)
	                        									# statr=Node(3)'s left=None, traversal="1-2-3-"

	                        				def preorder_print(self, start, traversal):

	                                            if start: # start=None

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.preorder_print(start.left, traversal)
	                                                traversal = self.preorder_print(start.right, traversal)

	                                            return traversal # traversal = "1-2-3-"

	                        				
	                            traversal = self.preorder_print(start.right, traversal)
	                            								# statr=Node(3)'s right=None, traversal="1-2-3-"

	                                        def preorder_print(self, start, traversal):

	                                            if start: # start=None

	                                                traversal += (str(start.value) + "-")
	                                                traversal = self.preorder_print(start.left, traversal)
	                                                traversal = self.preorder_print(start.right, traversal)

	                                            return traversal # traversal = "1-2-3-"
	                            
	                        return traversal # traversal = "1-2-3-"
	        			
	    return traversal # traversal = "1-2-3-"
















