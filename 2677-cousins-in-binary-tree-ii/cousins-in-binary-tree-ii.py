# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum_level = defaultdict(int)
        queue = deque([root])
        curr_level = 0
        while queue:
            l = len(queue)
            tmp = 0
            for _ in range(l):
                node = queue.popleft()
                tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sum_level[curr_level] = tmp
            curr_level += 1
        curr_level = 0
        queue = deque([root])
        root.val = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                value = 0
                if node.left:
                    value += node.left.val
                if node.right:
                    value += node.right.val
                if node.left:
                    node.left.val = sum_level[curr_level + 1] - value
                    queue.append(node.left)
                if node.right:
                    node.right.val = sum_level[curr_level + 1] - value
                    queue.append(node.right)
            curr_level += 1
        return root