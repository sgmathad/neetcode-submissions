# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        follower, traverser = head, head
        prev = head
        for _ in range(1, n):
            traverser = traverser.next

        while traverser and traverser.next:
            prev = follower
            follower = follower.next
            traverser = traverser.next
        
        if prev == follower:
            return prev.next
        
        prev.next = follower.next

        return head