# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        
        i = 0
        
        while i<n:
            first = first.next
            i+=1
        
        while first.next != None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
        
        