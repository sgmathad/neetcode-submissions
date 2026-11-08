# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        follower, traverser = head, head.next

        while traverser:
            if follower.val == traverser.val:
                follower.next = traverser.next
            else:
                follower = traverser
            
            traverser = traverser.next
        
        return head
