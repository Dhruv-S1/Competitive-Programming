# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = [-1]
        def recurse(node):
            if(node.left == None and node.right == None):
                return [node.val, node.val]
            elif(node.left == None):
                temp = recurse(node.right)
                min1 = min(temp[0], node.val)
                max1 = max(temp[1], node.val)
                ans[0] = max(max(abs(node.val - min1), abs(node.val - max1)), ans[0])
            elif(node.right == None):
                temp = recurse(node.left)
                min1 = min(temp[0], node.val)
                max1 = max(temp[1], node.val)
                ans[0] = max(max(abs(node.val - min1), abs(node.val - max1)), ans[0])
            else:
                min1 = min(recurse(node.left)[0], recurse(node.right)[0], node.val)
                max1 = max(recurse(node.left)[1], recurse(node.right)[1], node.val)
                ans[0] = max(max(abs(node.val - min1), abs(node.val - max1)), ans[0])
            return [min1, max1]
        recurse(root);
        return ans[0]
            
        
