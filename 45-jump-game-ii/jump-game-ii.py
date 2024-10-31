class Solution:
    def jump(self, nums: List[int]) -> int:
        i, j = 0, 0
        cnt = 0
        while i < len(nums):
            if j >= len(nums) - 1:
                return cnt
            max_j = j
            while i <= j:
                max_j = max(max_j, i + nums[i])
                i += 1
            j = max_j
            cnt += 1
            