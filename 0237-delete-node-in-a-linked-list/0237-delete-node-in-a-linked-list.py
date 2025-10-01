# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        prev_node = node
        curr_node = prev_node.next
        while curr_node.next != None:
            prev_node.val = curr_node.val
            curr_node = curr_node.next
            prev_node = prev_node.next
        
        prev_node.val = curr_node.val
        prev_node.next = None
        
        
        
        