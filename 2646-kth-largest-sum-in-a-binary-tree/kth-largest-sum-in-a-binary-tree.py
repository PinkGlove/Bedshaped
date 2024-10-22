# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        res = []
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
            heapq.heappush(res, -tmp)
        if len(res) < k:
            return -1
        for _ in range(k - 1):
            heapq.heappop(res)
        return -heapq.heappop(res)