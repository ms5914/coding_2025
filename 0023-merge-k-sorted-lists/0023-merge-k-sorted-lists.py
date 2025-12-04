# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) ==1:
            return lists[0]
        if not lists:
            return None

        interval = 1
        total_lists = len(lists)

        
        while interval<total_lists:
            i = 0
            while i<total_lists-interval:
                next_list = i+interval
                lists[i] = self.merge(lists[i], lists[next_list])
                i+=interval*2
            interval*=2
        return lists[0]


    def merge(self, li1, li2):
        dummy = ListNode()
        current = dummy

        while li1 and li2:
            if li1.val<=li2.val:
                current.next = li1
                li1 = li1.next
                current = current.next
            else:
                current.next = li2
                li2 = li2.next
                current = current.next
        
        if li1:
            current.next = li1
        elif li2:
            current.next = li2
        
        return dummy.next
        

