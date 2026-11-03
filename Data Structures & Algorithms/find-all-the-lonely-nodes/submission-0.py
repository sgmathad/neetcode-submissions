# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left and not node.right:
                result.append(node.left.val)

            elif not node.left and node.right:
                result.append(node.right.val)   

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)


        return result

