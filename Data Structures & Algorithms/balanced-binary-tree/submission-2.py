# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def height(root):
            nonlocal result
            if not result or not root:
                return 0
            
            x = height(root.left)
            y = height(root.right)
            
            if result and abs(x - y) > 1:
                result = False
            
            return max(x, y) + 1
            
        height(root)
        return result
            
