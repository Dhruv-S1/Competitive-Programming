# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None ):
            return head
        first  = head
        second = first.next
        secondTemp = second
        count = 0
        while(True):
            if(second.next == None):
                if(count % 2 == 1):
                    first.next = second.next
                    last = second
                    second.next = secondTemp
                else:
                    first.next = secondTemp
                break
            count += 1
            first.next = second.next;
            temp = second
            second = first.next
            first = temp
        return head
        
