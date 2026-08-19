# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        traverser = root

        while traverser or stack:
            if traverser:
                stack.append(traverser)
                traverser = traverser.left
            
            else:
                traverser = stack.pop()
                output.append(traverser.val)
                traverser = traverser.right
        return output