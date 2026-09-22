# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        follower, traverser = head, head

        while traverser:
            traverser = traverser.next
            if traverser:
                follower = follower.next
                traverser = traverser.next
        
        return follower