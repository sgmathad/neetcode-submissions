# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        while root or stack:
            if root:
                stack.append((root, 0))
                root = root.left
            
            else:
                root, visited = stack.pop()
                if visited:
                    result.append(root.val)
                    root = None
                else:
                    stack.append((root, 1))
                    root = root.right
        return result