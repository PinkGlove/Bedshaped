class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for _, num in cnt.items():
            if num % 2:
                return False
        return True