class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if stack and c in d and stack[-1] == d[c]:
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
