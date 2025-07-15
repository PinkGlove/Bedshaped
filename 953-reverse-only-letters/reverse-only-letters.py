class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        c = list(s)
        l, r = 0, len(c) - 1
        while l < r:
            while l < len(c) and not ('a' <= c[l] <= 'z' or 'A' <= c[l] <= 'Z'):
                l += 1
            while r >= 0 and not ('a' <= c[r] <= 'z' or 'A' <= c[r] <= 'Z'):
                r -= 1
            if l < r:
                c[l], c[r] = c[r], c[l]
                l += 1
                r -= 1
        return "".join(c)