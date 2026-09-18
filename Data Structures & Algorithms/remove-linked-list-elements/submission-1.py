# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        while head and head.val == val:
            head = head.next
        
        traverser = head
        follower = None

        while traverser:
            if traverser.val == val:
                follower.next = traverser.next
            
            else:
                follower = traverser
            
            traverser = traverser.next
        
        return head