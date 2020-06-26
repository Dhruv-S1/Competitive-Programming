# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = headA
        temp1 = headB
        count = 0
        if(headA == None or headB == None):
            return None
        while(True):
            if(headA == None):
                count += 1
                if(count == 2):
                    return None
                headA = temp1
            if(headB == None):
                headB = temp
            if(headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
            
