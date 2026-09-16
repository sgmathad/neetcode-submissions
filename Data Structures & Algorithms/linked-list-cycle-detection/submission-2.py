# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        traverser, follower = head, head

        while traverser:
            traverser = traverser.next
        
            if traverser == follower:
                return True

            if traverser:
                traverser = traverser.next
                follower = follower.next

        return False
