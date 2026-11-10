# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        follower, traverser = head, head.next

        while traverser and traverser.next:
            if traverser.val == 0:
                follower.next = traverser
                follower = follower.next
            else:
                follower.val += traverser.val
            traverser = traverser.next
        
        follower.next = None

        return head