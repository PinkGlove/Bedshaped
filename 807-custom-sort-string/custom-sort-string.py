class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = []
        for c in order:
            while cnt[c] > 0:
                res.append(c)
                cnt[c] -= 1
            del cnt[c]
        for k, v in cnt.items():
            while v > 0:
                res.append(k)
                v -= 1
        return "".join(res)