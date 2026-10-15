# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        traverser = head
        follower = head
        while traverser:
            for _ in range(m):
                if not traverser:
                    break
                follower = traverser
                traverser = traverser.next
            
            for _ in range(n):
                if not traverser:
                    break
                traverser = traverser.next
            
            if traverser:
                follower.next = traverser
            
            else: follower.next = None
        
        return head