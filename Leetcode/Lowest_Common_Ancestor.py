# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, depth):
            if(not node):
                return [depth-1, 0]
            a = dfs(node.left, depth+1)
            b = dfs(node.right, depth+1)
            if(a[0] > b[0]):
                return [a[0], a[1]]
            if(b[0] > a[0]):
                return [b[0], b[1]]
            if(b[0] == a[0]):
                return [b[0], node]
        a = dfs(root, 0)
        return a[1]
