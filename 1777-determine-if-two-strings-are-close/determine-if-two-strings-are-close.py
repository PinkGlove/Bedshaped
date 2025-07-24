class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1, l2 = [0] * 26, [0] * 26
        for c in word1:
            l1[ord(c) - ord('a')] += 1
        for c in word2:
            l2[ord(c) - ord('a')] += 1
        for i in range(len(l1)):
            if (l1[i] > 0 and l2[i] == 0) or (l1[i] == 0 and l2[i] > 0):
                return False
        return sorted(l1) == sorted(l2)