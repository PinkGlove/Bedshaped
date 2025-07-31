class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            cnt = 0
            while stack and heights[stack[-1][0]] <= h:
                prev_i, prev_h = stack.pop()
                res[prev_i] = cnt + 1
                cnt = prev_h + 1
            stack.append((i, cnt))
        cnt = 0
        while stack:
            i, h = stack.pop()
            res[i] = cnt
            cnt = h + 1
        return res
            