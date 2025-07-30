class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        t, res = [], []
        minimum = 'a'
        for c in s:
            t.append(c)
            cnt[c] -= 1
            while minimum <= 'z' and cnt[minimum] == 0:
                minimum = chr(ord(minimum) + 1)
            while t and t[-1] <= minimum:
                res.append(t.pop())
        return "".join(res)