# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        h2 = None
        t2 = None

        dummy = ListNode(0)
        dummy.next = head
        
        follower, traverser = dummy, head

        while traverser:
            if traverser.val >= x:
                follower.next = traverser.next
                if not h2:
                    h2 = traverser
                    t2 = h2
                else:
                    t2.next = traverser
                    t2 = t2.next
                traverser.next = None
                traverser = follower.next
            
            else:
                follower = traverser
                traverser = traverser.next

        follower.next = h2
        return dummy.next


