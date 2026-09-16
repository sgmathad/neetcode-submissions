# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(follower, traverser):
            nonlocal head
            if not traverser:
                head = follower
                return head
            reverse(traverser, traverser.next)
            traverser.next = follower

            return head

        return reverse(None, head)
