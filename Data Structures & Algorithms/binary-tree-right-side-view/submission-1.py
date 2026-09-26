# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        queue = [root]
        
        while queue:
            right_most = None
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    right_most = node.left.val
                
                if node.right:
                    queue.append(node.right)
                    right_most = node.right.val
            
            if right_most:
                result.append(right_most)
        return result