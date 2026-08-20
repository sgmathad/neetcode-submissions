# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        traverser = head
        follower = None

        while traverser and traverser.val == val:
            traverser = traverser.next
            head = traverser

        while traverser:
            if traverser.val == val:
                follower.next = traverser.next
            else:
                follower = traverser
            traverser = traverser.next
    
        return head

