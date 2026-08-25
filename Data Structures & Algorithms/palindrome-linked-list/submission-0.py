# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        def find_middle(head):
            if not head:
                return None
            
            follower, traverser = head, head

            while traverser:
                traverser = traverser.next
                if traverser and traverser.next:
                    traverser = traverser.next
                    follower = follower.next
            
            return follower
        
        def reverse(head):
            if not head:
                return head
            
            new = None
            follower, traverser = None, head

            while traverser:
                follower = traverser
                traverser = traverser.next
                follower.next = new
                new = follower
            
            return new
        
        middle = find_middle(head)
        t1, t2 = head, reverse(middle.next)

        while t1 and t2:
            if t1.val != t2.val:
                return False
            
            t1 = t1.next
            t2 = t2.next
        
        return True

        
