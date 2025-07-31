class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0] * len(arr)
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                stack.pop()
            if stack:
                res[i] = res[stack[-1]] + (i - stack[-1]) * num
            else:
                res[i] = (i + 1) * num
            stack.append(i)
        return sum(res) % (10 ** 9 + 7)