# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
ans = 0
marker = [0, 0]

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            global ans
            global marker
            if(node == None):
                return -99999
            temp = dfs(node.left)
            temp1 = dfs(node.right)
            print(temp, temp1)
            if(temp!= -99999 and temp1!= -99999):
                ans = node
                return -99999
            if(node.val == p.val and (temp!=-99999 or temp1!=-99999)):
                ans = node
                return -99999
            if(node.val == q.val and (temp!=-99999 or temp1!=-99999)):
                ans = node
                return -99999
            if(node.val == p.val):
                return p.val
            if(node.val == q.val):
                return q.val
            if(temp != -99999):
                return temp
            if(temp1 != -99999):
                return temp1
            return -99999
            
        dfs(root)
        return ans
            
            
            
        
