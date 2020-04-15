# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def check_same(rootA, rootB):

            if(rootA == None and rootB == None):
                return True
            if(rootB == None and rootA == None):
                return True
            if(rootA == None and rootB != None):
                return False
            if(rootA != None and rootB == None):
                return False
            if(rootA.val != rootB.val):
                return False;
            else:
                return (check_same(rootA.left, rootB.right)  and check_same(rootA.right, rootB.left)) or (check_same(rootA.right, rootB.right) and check_same(rootA.left, rootB.left))
        return check_same(root1, root2)
           
            
            
        
