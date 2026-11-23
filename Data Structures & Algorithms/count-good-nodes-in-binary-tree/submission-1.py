# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 1
        queue = [(root, root.val)]

        while queue:
            node, greater = queue.pop(0)

            if node.left:
                l_greater = greater
                if greater <= node.left.val:
                    l_greater = node.left.val
                    result += 1
                queue.append((node.left, l_greater))
            
            if node.right:
                r_greater = greater
                if greater <= node.right.val:
                    r_greater = node.right.val
                    result += 1
                queue.append((node.right, r_greater))
        return result