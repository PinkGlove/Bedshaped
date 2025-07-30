class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                res += i - stack[-1]
                stack.pop()
            stack.append(i)
        while stack:
            res += len(nums) - stack.pop()
        return res