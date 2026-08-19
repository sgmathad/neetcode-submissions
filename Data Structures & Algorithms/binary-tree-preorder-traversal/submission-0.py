# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        traverser = root

        while traverser or stack:
            if traverser:
                output.append(traverser.val)
                stack.append(traverser)
                traverser = traverser.left
            else:
                traverser = stack.pop()
                traverser = traverser.right
        
        return output