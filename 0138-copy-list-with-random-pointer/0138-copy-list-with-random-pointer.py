"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        
        head1 = head
        # 1->1'->2->2'
        while head1:
            ptr = Node(head1.val)
            ptr.next = head1.next 
            head1.next = ptr
            head1 = ptr.next
  

        new_list = head.next
        old_list = head

        while old_list:
            new_list.random =  old_list.random.next if old_list.random else None
            old_list = old_list.next.next if old_list.next else None
            new_list = new_list.next.next if new_list.next else None
        
        # ptr = head.next
        
        #a-a'-b-b'
# Corrected Separation Logic
        old_list = head
        new_list, ptr = head.next, head.next # ptr holds the new head, which is correct

        while old_list:
            old_list.next = new_list.next
            new_list.next = old_list.next.next if old_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        
        return ptr




        