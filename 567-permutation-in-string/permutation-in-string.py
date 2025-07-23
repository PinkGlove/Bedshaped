class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = [0] * 26, [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            l2[ord(s2[r]) - ord('a')] += 1
            while r - l + 1 > len(s1):
                l2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if r - l + 1 == len(s1) and l1 == l2:
                return True
        return False