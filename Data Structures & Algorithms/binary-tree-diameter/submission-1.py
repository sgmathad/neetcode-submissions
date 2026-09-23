# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def height(root):
            nonlocal result
            if not root:
                return 0
            
            x = height(root.left)
            y = height(root.right)

            result = max(result, (x + y))

            return max(x, y) + 1

        height(root)
        
        return result