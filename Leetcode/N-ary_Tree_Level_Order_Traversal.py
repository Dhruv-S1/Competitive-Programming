"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        for i in range(1001):
            ans.append([])
        
        def search(root, hieght):
            if(root == None): 
                return
            ans[hieght].append(root.val)
            for i in range(len(root.children)):
                search(root.children[i], hieght + 1)
        search(root, 0)
        for i in range(len(ans)-1, -1, -1):
            if(ans[i] == []):
                ans.pop()
            else:
                break
        return ans
        
        
