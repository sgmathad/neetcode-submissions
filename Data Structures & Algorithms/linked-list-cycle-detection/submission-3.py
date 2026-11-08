# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        follower, traverser = head, head

        while traverser:
            traverser = traverser.next

            if follower == traverser:
                return True

            if traverser:
                follower = follower.next
                traverser = traverser.next
            
        return False
