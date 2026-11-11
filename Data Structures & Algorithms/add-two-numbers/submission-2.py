# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        l3 = None
        t3 = None
        carry = 0

        def add_node(value):
            nonlocal l3, t3
            carry = 0
            if value > 9:
                value %= 10
                carry = 1
            
            node = ListNode(value)
            if not l3:
                l3 = node
                t3 = l3
            else:
                t3.next = node
                t3 = node
            
            return carry

        while t1 and t2:
            value = carry + t1.val + t2.val
            carry = add_node(value)
            t1 = t1.next
            t2 = t2.next
        
        while t1:
            value = carry + t1.val
            carry = add_node(value)
            t1 = t1.next
        
        while t2:
            value = carry + t2.val      
            carry = add_node(value)
            t2 = t2.next
        
        if carry:
            t3.next = ListNode(carry)

        return l3