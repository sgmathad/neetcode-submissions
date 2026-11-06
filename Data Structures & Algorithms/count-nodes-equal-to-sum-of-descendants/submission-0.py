# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        result = 0

        def postorder(root):
            nonlocal result
            if not root:
                return 0
            
            left = postorder(root.left)
            right = postorder(root.right)

            if root.val == left + right:
                result += 1
            
            return root.val + left + right
        
        postorder(root)
        return result