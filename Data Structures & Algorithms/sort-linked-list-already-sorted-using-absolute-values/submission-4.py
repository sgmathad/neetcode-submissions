# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        nums = []

        while head and head.val < 0:
            heapq.heappush(nums, head.val)
            head = head.next
        
        follower, traverser = head, head

        while traverser:
            if traverser.val < 0:
                follower.next = traverser.next
                heapq.heappush(nums, traverser.val)
            else:
                follower = traverser
            
            traverser = traverser.next

        if nums:
            nl = ListNode(heapq.heappop(nums))
            nh = nl

            while nums:
                node = ListNode(heapq.heappop(nums))
                nl.next = node
                nl = node

            nl.next = head
            return nh
        
        return head







