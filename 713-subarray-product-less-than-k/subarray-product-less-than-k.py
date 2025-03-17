class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j, cnt = 0, 0, 1
        res = 0
        while j < len(nums):
            cnt *= nums[j]
            while i <= j and cnt >= k:
                cnt /= nums[i]
                i += 1
            res += (j - i + 1)
            j += 1
        return res