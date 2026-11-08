# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        follower, traverser = head, head

        for _ in range(1, k):
            traverser = traverser.next
        
        a = traverser # for swapping later

        while traverser and traverser.next:
            follower = follower.next
            traverser = traverser.next
        
        b = follower

        a.val, b.val = b.val, a.val

        return head