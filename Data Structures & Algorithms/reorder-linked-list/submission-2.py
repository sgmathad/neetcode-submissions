# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        
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
        
        stack = []
        mid = middle(head)
        t2 = mid.next
        mid.next = None

        while t2:
            stack.append(t2)
            t2 = t2.next
        
        t1 = head
        while stack:
            node = stack.pop()
            node.next = t1.next
            t1.next = node
            t1 = node.next

        return
            
