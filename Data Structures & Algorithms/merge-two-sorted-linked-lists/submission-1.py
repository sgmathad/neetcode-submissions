# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        merger, list3 = None, None

        if list1.val < list2.val:
            merger = list1
            list1 = list1.next
        else:
            merger = list2
            list2 = list2.next
            
        list3 = merger

        while list1 and list2:
            if list1.val < list2.val:
                merger.next = list1
                list1 = list1.next
            
            else:
                merger.next = list2
                list2 = list2.next
            
            merger = merger.next

        if list1:
            merger.next = list1
        
        if list2:
            merger.next = list2

        return list3