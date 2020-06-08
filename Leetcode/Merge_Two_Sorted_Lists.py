# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = None
        start = None
        while(True):
            if(node != None):
                print(node.val)
            if(l1 == None and l2 == None):
                break
            if(l1 == None):
                if(node == None):
                    node = l2
                    start = node
                    l2 = l2.next
                    continue
                node.next = l2
                l2 = l2.next
                node = node.next
                continue
            if(l2 == None):
                if(node == None):
                    node = l1
                    start = node
                    l1 = l1.next
                    continue
                node.next = l1
                l1 = l1.next
                node = node.next
                continue
            if(l1.val <= l2.val):
                if(node == None):
                    node = l1
                    start = node
                else:
                    node.next = l1
                    node = node.next
                l1 = l1.next
            else:
                if(node == None):
                    node = l2
                    start = node
                else:
                    node.next = l2
                    node = node.next
                l2 = l2.next
                
        return start
    
        
