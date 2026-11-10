# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        l2_last = list2

        # to get the l2 last node
        while l2_last and l2_last.next:
            l2_last = l2_last.next
        
        follower, traverser = head, head

        for _ in range(a):
            follower = traverser
            traverser = traverser.next
        
        follower.next = list2

        for _ in range(a, b):
            traverser = traverser.next
        
        l2_last.next = traverser.next

        return head