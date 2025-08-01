# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, cnt = stack.pop()
            if cnt == targetSum and not node.left and not node.right:
                return True
            if node.left:
                stack.append((node.left, node.left.val + cnt))
            if node.right:
                stack.append((node.right, node.right.val + cnt))
        return False