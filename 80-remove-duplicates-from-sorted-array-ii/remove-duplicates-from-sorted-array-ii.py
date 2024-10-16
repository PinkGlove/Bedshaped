class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        cnt = 1
        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                if cnt < 2:
                    nums[left] = nums[right]
                    left += 1
                cnt += 1
            else:
                nums[left] = nums[right]
                cnt = 1
                left += 1
        return left