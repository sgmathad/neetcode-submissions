# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        last = head
        count = 1

        while last and last.next:
            last = last.next
            count += 1
        
        k = k % count

        if k == 0:
            return head
        
        mover = head
        for _ in range(k):
            mover = mover.next
        
        follower, traverser = head, head

        while mover:
            follower = traverser
            traverser = traverser.next
            mover = mover.next
        
        follower.next = None
        last.next = head

        return traverser
