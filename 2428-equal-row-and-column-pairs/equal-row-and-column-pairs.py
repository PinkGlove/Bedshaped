class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(lambda: [0, 0])
        for i in range(len(grid)):
            d[tuple(grid[i])][0] += 1
            curr = []
            for j in range(len(grid[0])):
                curr.append(grid[j][i])
            d[tuple(curr)][1] += 1
        res = 0
        for v in d.values():
            res += v[0] * v[1]
        return res
            