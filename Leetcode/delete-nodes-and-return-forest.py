# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def traverseTree(root):
            if(root == None): return
            if(root.val in to_delete_set):
                if(root.left != None):
                    roots.add(root.left)
                if(root.right != None):
                    roots.add(root.right)
                if(root in roots):
                    roots.remove(root)
            traverseTree(root.left)
            traverseTree(root.right) 
            if(root.left != None):
                if(root.left.val in to_delete_set):
                    root.left = None
            if(root.right != None):
                if(root.right.val in to_delete_set):
                    root.right = None
        roots = set()
        roots.add(root)
        to_delete_set = set()
        for i in range(len(to_delete)):
            to_delete_set.add(to_delete[i])
        traverseTree(root)
        ans = []
        for a in roots:
            ans.append(a)
        return ans
            
        
