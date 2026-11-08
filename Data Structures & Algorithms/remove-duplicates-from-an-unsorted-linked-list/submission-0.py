# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        mapper = {}

        traverser = head

        while traverser:
            value = traverser.val
            mapper[value] = mapper.get(value, 0) + 1
            traverser = traverser.next
        
        while head and mapper[head.val] > 1:
            head = head.next
        
        follower, traverser = head, head

        while traverser:
            if mapper[traverser.val] > 1:
                follower.next = traverser.next
            else:
                follower = traverser
            
            traverser = traverser.next
        
        return head