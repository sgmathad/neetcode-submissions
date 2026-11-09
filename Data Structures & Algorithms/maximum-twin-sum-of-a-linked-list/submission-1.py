# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        _max = 0
        follower, traverser = head, head

        while traverser:
            traverser = traverser.next

            if traverser:
                stack.append(follower.val)
                follower = follower.next
                traverser = traverser.next

        while follower:
            _max = max(_max, stack.pop() + follower.val)
            follower = follower.next

        return _max
        