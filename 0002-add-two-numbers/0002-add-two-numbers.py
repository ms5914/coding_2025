# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode(0, None)
        head = dummyNode

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_result = val1+val2+carry
            carry = sum_result//10
            sum_result = sum_result%10
            head.next = ListNode(sum_result)
            
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyNode.next


        
        

        