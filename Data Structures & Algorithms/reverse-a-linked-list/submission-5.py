# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(traverser, follower):
            nonlocal head
            if not traverser:
                head = follower
                return

            reverse(traverser.next, traverser)
            traverser.next = follower
            return
        
        reverse(head, None)
        return head