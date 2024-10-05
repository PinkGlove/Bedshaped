class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = Counter(s1)
        cnt_s2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            cnt_s2[s2[r]] += 1
            while cnt_s2[s2[r]] > cnt_s1[s2[r]]:
                cnt_s2[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False