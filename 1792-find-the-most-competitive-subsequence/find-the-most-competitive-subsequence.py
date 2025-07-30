class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                if i >= len(nums) - k and len(stack) <= k - (len(nums) - i):
                    break
                stack.pop()
            if len(stack) < k:
                stack.append(i)
        return [nums[i] for i in stack]

        # 3 3 5 3 2 6 1   k = 3