# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and not q or q and not p:
            return False
        elif p.val != q.val:
            return False
        else:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        