# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
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
        
        def add(head):
            if not head:
                return head
            
            traverser = head
            follower = head
            traverser.val += 1
            carry = 0

            while traverser:
                traverser.val += carry
                if traverser.val > 9:
                    traverser.val %= 10
                    carry = 1
                else:
                    carry = 0
                    break
                
                follower = traverser
                traverser = traverser.next
            
            if carry == 1:
                follower.next = ListNode(1)
            
            return head
        
        head = reverse(head)
        head = add(head)
        head = reverse(head)

        return head