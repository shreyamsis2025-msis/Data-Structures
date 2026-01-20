class BinarysearchtreeNode:
    class __node__:
        def __init__(self, ele):
            self.data = ele
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
        self.count=0
        
    #a. check BST is empty
    def is_empty(self):
        return self.count==0
    
    #b. Get count of nodes in BST
    def getcount(self):
        return self.count
    
    #c. Add nodes to BST
    def add_element(self,ele):
        cur_node =par_node = self.root
        while cur_node !=None and cur_node.data!=ele:
            par_node = cur_node
            if ele<cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        if cur_node ==None:
            new_node = self.__node__(ele)
            if par_node !=None:
                if ele<par_node.data:
                    par_node.left = new_node
                else:
                    par_node.right = new_node
            else:
                self.root = new_node
            self.count+=1
            
    #Search noe in BST
    def is_memeber(self,key):
        cur = self.root
        while cur !=None:
            if key<cur.data:
                cur = cur.left
            elif key>cur.data:
                cur = cur.right
            else:
                break
        return cur!=None
    
    #e. Tree Traversals 
      #1. Inorder Traversal
    def bst_inorder(self):
        if not self.is_empty():
            self.__inorder__(self.root)
    
    def __inorder__(self,node):
        if node !=None:
            self.__inorder__(node.left)
            print(node.data,end=" ")
            self.__inorder__(node.right)
            
      #2. Preorder Traversal
    def bst_preorder(self):
        if not self.is_empty():
            self.__preorder__(self.root)
            
    def __preorder__(self,node):
        if node !=None:
            print(node.data,end=" ")
            self.__preorder__(node.left)
            self.__preorder__(node.right)
            
      #3. Postorder Traversal
    def bst_postorder(self):
        if not self.is_empty():
            self.__postorder__(self.root)
            
    def __postorder__(self,node):
        if node !=None:
            self.__postorder__(node.left)
            self.__postorder__(node.right)
            print(node.data,end=" ")
            
      #4. Level order Traversal
    def bst_levelorder(self):
        if not self.is_empty():
            self.__levelorder__(self.root)
            
    def __levelorder__(self,node):
        queue=[]
        queue.append(node)
        while len(queue)>0:
            cur = queue.pop(0)
            print(cur.data,end=" ")
            if cur.left !=None:
                queue.append(cur.left)
            if cur.right !=None:
                queue.append(cur.right)
                
    #f. Delete Specified node from BST
    def delete_node(self, key):
        if not self.is_empty():
            self.root = self.__node_delete__(self.root, key)

    def __node_delete__(self, node, key):
        if node is None:
            return None
        elif key < node.data:
            node.left = self.__node_delete__(node.left, key)
        elif key > node.data:
            node.right = self.__node_delete__(node.right, key)
        elif node.left and node.right:
            temp = self.__find_min__(node.right)
            node.data = temp.data
            node.right = self.__node_delete__(node.right, node.data)
        else:
            if node.left is None:
                node = node.right
            else:
                node = node.left
        return node

    def __find_min__(self, node):
        if node.left is None:
            return node
        else:
            return self.__find_min__(node.left)
        
    #g. Find Height of BST
    def find_height(self):
        if not self.is_empty():
            return self.__height__(self.root)
        return -1
    
    def __height__(self,node):
        if node ==None:
            return -1
        else:
            return 1+max(self.__height__(node.left),self.__height__(node.right))
        
    #h. count number of terminal nodes in BST
    def count_terminal_nodes(self):
        if not self.is_empty():
            return self.__terminal_count__(self.root)
        return 0
    def __terminal_count__(self,node):
        if node ==None:
            return 0
        elif node.left ==None and node.right ==None:
            return 1
        else:
            return self.__terminal_count__(node.left)+self.__terminal_count__(node.right)
        
    
            
#test
if __name__=="__main__":    
    bst = BinarysearchtreeNode()
    lst = [15,10,20,8,12,17,25]
    for ele in lst:
        bst.add_element(ele)
    print("Inorder Traversal of BST is:")
    bst.bst_inorder()
    print()
    print("Preorder Traversal of BST is:")
    bst.bst_preorder()
    print()
    print("Postorder Traversal of BST is:")
    bst.bst_postorder()
    print()
    print("Level order Traversal of BST is:")
    bst.bst_levelorder()
    print()
    key = 17
    if bst.is_memeber(key):
        print(f"{key} is present in BST")
    else:
        print(f"{key} is not present in BST")
        
    key = 19
    if bst.is_memeber(key):
        print(f"{key} is present in BST")
    else:
        print(f"{key} is not present in BST")
        
    print(f"Total number of nodes in BST is: {bst.getcount()}")
    
    height = bst.find_height()
    print(f"Height of BST is: {height}")
    
    term_count = bst.count_terminal_nodes()
    print(f"Total number of terminal nodes in BST is: {term_count}")
    
    del_key = 10
    print(f"Delete node {del_key} from BST")
    bst.delete_node(del_key)
    print("Inorder Traversal of BST is:")
    bst.bst_inorder()
    print()         
    