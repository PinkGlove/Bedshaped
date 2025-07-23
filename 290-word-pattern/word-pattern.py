class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        dp = defaultdict(str)
        ds = defaultdict(str)
        for i, c in enumerate(pattern):
            if c in dp and dp[c] != words[i]:
                return False
            if words[i] in ds and ds[words[i]] != c:
                return False
            dp[c] = words[i]
            ds[words[i]] = c
        return True