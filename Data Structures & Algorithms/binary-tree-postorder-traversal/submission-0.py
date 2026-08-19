# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        stack2 = []
        output = []
        traverser = root

        while traverser or stack:
            if traverser:
                stack.append(traverser)
                traverser = traverser.left
            else:
                traverser = stack.pop()

                if stack2 and stack2[-1] == traverser:
                    stack2.pop()
                    output.append(traverser.val)
                    traverser = None
                else:
                    stack2.append(traverser)
                    stack.append(traverser)
                    traverser = traverser.right
        return output