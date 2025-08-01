# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, maximum = stack.pop()
            if node.val >= maximum:
                res += 1 
            maximum = max(maximum, node.val)
            if node.left:
                stack.append((node.left, maximum))
            if node.right:
                stack.append((node.right, maximum))
        return res
