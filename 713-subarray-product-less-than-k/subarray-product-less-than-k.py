class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r, cnt = 0, 0, 1
        res = 0
        while r < len(nums):
            cnt *= nums[r]
            while l <= r and cnt >= k:
                cnt /= nums[l]
                l += 1
            res += (r - l + 1)
            r += 1
        return res