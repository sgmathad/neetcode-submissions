"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
            
        head = Node(node.val)
        queue = [(node, head)]
        visited = set()
        visited.add(node)
        copy = {node: head}

        while queue:
            n1, n2 = queue.pop(0)
            for nei in n1.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    new_nei = Node(nei.val)
                    n2.neighbors.append(new_nei)
                    copy[nei] = new_nei
                    queue.append((nei, new_nei))
                
                else:
                    n2.neighbors.append(copy[nei])

        return head