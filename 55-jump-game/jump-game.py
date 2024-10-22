class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for num in nums:
            if steps < 0:
                return False
            if num > steps:
                steps = num
            steps -= 1
        return True
                    