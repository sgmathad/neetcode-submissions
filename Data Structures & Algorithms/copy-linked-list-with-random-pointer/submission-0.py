"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        head2 = Node(head.val)
        t2 = head2

        t1 = head.next

        mapper = {head: head2}

        while t1:
            new_node = Node(t1.val)
            t2.next = new_node
            mapper[t1] = new_node

            t1 = t1.next
            t2 = t2.next

        for a, b in mapper.items():
            if a.random:
                b.random = mapper[a.random]

        return head2




