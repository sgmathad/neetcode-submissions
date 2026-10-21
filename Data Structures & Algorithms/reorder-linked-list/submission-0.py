# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def middle(head):
            if not head:
                return head

            follower, traverser = head, head

            while traverser:
                traverser = traverser.next
                if traverser:
                    follower = follower.next
                    traverser = traverser.next
            return follower
        

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
        
        if not head:
            return head

        mid = middle(head)
        h2 = mid.next
        mid.next = None

        h2 = reverse(h2)

        t1, t2 = head, h2

        while t1 and t2:
            next1 = t1.next
            next2 = t2.next
            
            t1.next = t2
            t2.next = next1
            
            t1 = next1
            t2 = next2