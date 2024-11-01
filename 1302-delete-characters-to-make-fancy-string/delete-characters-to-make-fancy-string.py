class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            curr = s[i]
            cnt = 1
            i += 1
            while i < len(s) and s[i] == curr:
                i += 1
                cnt += 1
            for _ in range(min(cnt, 2)):
                res.append(curr)
        return "".join(res)