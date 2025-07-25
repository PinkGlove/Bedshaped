class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res = res & set(nums[i])
        return sorted(list(res))
