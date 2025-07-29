class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue, min_queue = deque(), deque()
        l = 0
        res = 0
        for r, num in enumerate(nums):
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            max_queue.append(r)
            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            min_queue.append(r)
            while max_queue and min_queue and abs(nums[max_queue[0]] - nums[min_queue[0]]) > limit:
                if max_queue[0] <= l:
                    max_queue.popleft()
                if min_queue[0] <= l:
                    min_queue.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res