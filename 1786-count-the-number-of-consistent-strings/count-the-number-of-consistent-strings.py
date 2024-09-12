class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def check(pattern, word):
            for c in word:
                if c not in pattern:
                    return False
            return True
        
        res = 0
        pattern = set(allowed)
        for word in words:
            if check(pattern, word):
                res += 1
        return res