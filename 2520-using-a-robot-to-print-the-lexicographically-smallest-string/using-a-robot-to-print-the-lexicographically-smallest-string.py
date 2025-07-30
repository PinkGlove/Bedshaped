class Solution:
    def robotWithString(self, s: str) -> str:
        t, res = [], []
        minimum = [0] * len(s)
        minimum[-1] = 'z'
        for i in range(len(s) - 1, 0, -1):
            minimum[i - 1] = min(minimum[i], s[i])
        for i, c in enumerate(s):
            t.append(c)
            while t and t[-1] <= minimum[i]:
                res.append(t.pop())
        return "".join(res)