class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l, r = 0, 0
        res = list(word)
        while res[r] != ch:
            r += 1
            if r == len(res):
                return word
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        return "".join(res)