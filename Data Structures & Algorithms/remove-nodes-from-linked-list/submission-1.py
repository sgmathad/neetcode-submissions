# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if not head:
                return head
            
            new = None
            follower, traverser = head, head

            while traverser:
                follower = traverser
                traverser = traverser.next
                follower.next = new
                new = follower
            
            return new
        
        if not head.next:
            return head

        head = reverse(head)

        follower, traverser = head, head.next

        while traverser:
            if follower.val > traverser.val:
                follower.next = traverser.next
            
            else:
                follower = traverser
            
            traverser = traverser.next

        return reverse(head)
