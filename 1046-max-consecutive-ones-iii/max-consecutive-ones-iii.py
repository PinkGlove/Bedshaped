class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j, cnt, res = 0, 0, 0, 0
        while j < len(nums):
            if nums[j] == 0:
                cnt += 1
            while cnt > k:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res