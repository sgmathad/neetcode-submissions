# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        
        if not list1:
            return list2

        list3 = None

        if list1.val < list2.val:
            list3 = list1
            list1 = list1.next
        
        else:
            list3 = list2
            list2 = list2.next
        
        merger = list3

        while list1 and list2:
            if list1.val < list2.val:
                merger.next = list1
                merger = list1
                list1 = list1.next
            else:
                merger.next = list2
                merger = list2
                list2 = list2.next
        

        if list1:
            merger.next = list1
        
        if list2:
            merger.next = list2
        

        return list3