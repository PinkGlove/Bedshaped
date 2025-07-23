class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0
        cnt = defaultdict(int)
        ps = [0]
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            ps.append(ps[-1] + nums[r])
            while cnt[nums[r]] > 1:
                cnt[nums[l]] -= 1
                l += 1
            res = max(res, ps[r + 1] - ps[l])
        return res