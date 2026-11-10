# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        start = ListNode(0)
        not_nine = start
        start.next = head

        # set not_nine to rightmost non 9 value
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next
        
        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        

        return start if start.val else start.next