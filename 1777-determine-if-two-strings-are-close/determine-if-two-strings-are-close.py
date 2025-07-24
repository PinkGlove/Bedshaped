class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.keys()) == sorted(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())