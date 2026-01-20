#modify a BST so that each node stores an extra field:size of its subtree
class BST:
    class __node__:
        def __init__(self,ele):
            self.data = ele
            self.left = None
            self.right = None
            self.size = 1
            
    def __init__(self):
        self.root = None
        self.count = 0
        
    def is_empty(self):
        return self.count==0
    
    def size(self):
        return self.count
    
    #Insert node in BST
    def insert(self,ele):
        self.root = self.__insert__(self.root,ele)
        self.count+=1
    def __insert__(self,node,ele):
        if node ==None:
            return self.__node__(ele)
        if ele<node.data:
            node.left = self.__insert__(node.left,ele)
        else:
            node.right = self.__insert__(node.right,ele)
        node.size = 1 + self.__get_size__(node.left) + self.__get_size__(node.right)
        return node
    
    def __get_size__(self,node):
        if node ==None:
            return 0
        return node.size    
    
    #Inorder Traversal
    def inorder(self):      
        if not self.is_empty():
            self.__inorder__(self.root)     
            
    def __inorder__(self,node):
        if node !=None:
            self.__inorder__(node.left)
            print(f"{node.data}({node.size})",end=" ")
            self.__inorder__(node.right)
            
    #test
if __name__=="__main__":
    bst = BST()
    lst = [15,10,20,8,12,17,25]
    for ele in lst:
        bst.insert(ele)
    print("Inorder Traversal of BST is:")
    bst.inorder()
    print()
    
    
    
# #modify a BST so that each node stores an extra field:size of its subtree
# class BST:
#     class __node__:
#         def __init__(self, ele):
#             self.data = ele
#             self.left = None
#             self.right = None
#             self.size = 1    # 👈 new field for subtree size

#     def __init__(self):
#         self.root = None

#     # helper to get size safely
#     def __get_size__(self, node):
#         return node.size if node else 0

#     # update size of a node
#     def __update_size__(self, node):
#         if node:
#             node.size = 1 + self.__get_size__(node.left) + self.__get_size__(node.right)

#     # insert element
#     def add_element(self, ele):
#         self.root = self.__insert__(self.root, ele)

#     def __insert__(self, node, ele):
#         if node is None:
#             return self.__node__(ele)
#         if ele < node.data:
#             node.left = self.__insert__(node.left, ele)
#         elif ele > node.data:
#             node.right = self.__insert__(node.right, ele)
#         # update size on the way back
#         self.__update_size__(node)
#         return node

#     # delete node
#     def delete_node(self, key):
#         self.root = self.__delete__(self.root, key)

#     def __delete__(self, node, key):
#         if node is None:
#             return None
#         if key < node.data:
#             node.left = self.__delete__(node.left, key)
#         elif key > node.data:
#             node.right = self.__delete__(node.right, key)
#         else:  # found the node
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             else:
#                 temp = self.__find_min__(node.right)
#                 node.data = temp.data
#                 node.right = self.__delete__(node.right, temp.data)

#         self.__update_size__(node)
#         return node

#     def __find_min__(self, node):
#         while node.left:
#             node = node.left
#         return node

#     # inorder traversal
#     def inorder(self):
#         self.__inorder__(self.root)
#         print()

#     def __inorder__(self, node):
#         if node:
#             self.__inorder__(node.left)
#             print(f"{node.data}({node.size})", end=" ")  # 👈 print size along with data
#             self.__inorder__(node.right)

#     # get size of whole BST
#     def get_size(self):
#         return self.__get_size__(self.root)

# #test
# if __name__ == "__main__":    
#     bst = BST()
#     lst = [15, 10, 20, 8, 12, 17, 25]
#     for ele in lst:
#         bst.add_element(ele)
#     print("Inorder Traversal of BST with subtree sizes:")
#     bst.inorder()
#     print(f"Size of the entire BST: {bst.get_size()}")
#     bst.delete_node(10)
#     print("Inorder Traversal after deleting 10:")
#     bst.inorder()
#     print(f"Size of the entire BST after deletion: {bst.get_size()}")