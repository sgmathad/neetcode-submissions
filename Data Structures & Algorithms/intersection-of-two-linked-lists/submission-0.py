# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):
            if not head:
                return 0
            
            traverser = head
            count = 0

            while traverser:
                count += 1
                traverser = traverser.next

            return count
        
        def traverse(head, k):
            if not head:
                return head
            
            for _ in range(k):
                head = head.next
            
            return head
        
        l1 = length(headA)
        l2 = length(headB)

        diff = abs(l1 - l2)

        if l1 >= l2:
            headA = traverse(headA, diff)
        else:
            headB = traverse(headB, diff)

        t1, t2 = headA, headB
        while t1 and t2:
            if t1 == t2:
                return t1
            t1 = t1.next
            t2 = t2.next
        
        return None
