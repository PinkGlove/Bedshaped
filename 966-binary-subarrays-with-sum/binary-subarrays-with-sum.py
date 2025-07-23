class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = defaultdict(int)
        curr = 0
        res = 0
        cnt[0] = 1
        for num in nums:
            curr += num
            if curr - goal in cnt:
                res += cnt[curr - goal]
            cnt[curr] += 1
        return res