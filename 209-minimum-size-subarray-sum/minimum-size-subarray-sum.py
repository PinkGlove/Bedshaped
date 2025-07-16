class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        res = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr - nums[l] >= target:
                curr -= nums[l]
                l += 1
            if curr >= target:
                if res == 0:
                    res = float('inf')
                res = min(res, r - l + 1)
        return res