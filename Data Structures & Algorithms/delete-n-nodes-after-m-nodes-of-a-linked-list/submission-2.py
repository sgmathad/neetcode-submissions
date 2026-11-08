# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        follower, traverser = head, head

        while traverser:
            for _ in range(m):
                if traverser:
                    follower = traverser
                    traverser = traverser.next

            for _ in range(n):
                if traverser:
                    traverser = traverser.next
            
            follower.next = traverser
        
        return head