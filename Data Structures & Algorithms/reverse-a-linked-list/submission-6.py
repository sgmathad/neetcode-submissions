# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(traverser, follower):
            if not traverser:
                head = follower
                return head

            head = reverse(traverser.next, traverser)
            traverser.next = follower
            return head
        
        head = reverse(head, None)
        return head