# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if not node:
                return 0
            left = dfs(node.left, max(maximum, node.val))
            right = dfs(node.right, max(maximum, node.val))
            res = left + right
            if node.val >= maximum:
                res += 1
            return res
        return dfs(root, float('-inf'))

