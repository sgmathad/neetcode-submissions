# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _range_sum(self, root: TreeNode, low: int, high: int, result: int)->int:
        if not root:
            return 0
        
        left = self._range_sum(root.left, low, high, result)
        right = self._range_sum(root.right, low, high, result)

        if low <= root.val <= high:
            result += root.val
        
        return result + left + right

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # if not root.left and not root.right:
        #     return root.val
        return self._range_sum(root, low, high, 0)