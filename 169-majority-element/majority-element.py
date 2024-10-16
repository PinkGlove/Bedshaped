class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, res = 0, nums[0]
        for i in range(len(nums) - 1):
            if nums[i] == res:
                curr += 1
            else:
                curr -= 1
            if curr <= 0:
                curr = 0
                res = nums[i + 1]
        return res
        