class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = [0] * len(s)
        for i in range(len(s)):
            nums[i] = abs(ord(s[i]) - ord(t[i]))
        l = 0
        curr, res = 0, 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > maxCost:
                curr -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res