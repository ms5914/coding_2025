# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        curr_node, fast_node = head, head
        prev_node = None
        next_node = None
        
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        if fast_node:
            curr_node = curr_node.next
            
            
        while prev_node and curr_node:
            if prev_node.val != curr_node.val:
                return False
            prev_node = prev_node.next
            curr_node = curr_node.next
        return True