class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        for c in s:
            if s1 and c == '#':
                s1.pop()
            elif c != '#':
                s1.append(c)
        for c in t:
            if s2 and c == '#':
                s2.pop()
            elif c != '#':
                s2.append(c)
        return s1 == s2