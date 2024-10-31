class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        for i in range(1, m):
            min_color, sec_min_color = None, None
            for j in range(n):
                if min_color == None or costs[i - 1][min_color] > costs[i - 1][j]:
                    sec_min_color = min_color
                    min_color = j
                elif sec_min_color == None or costs[i - 1][sec_min_color] > costs[i - 1][j]:
                    sec_min_color = j
            for j in range(n):
                if j == min_color:
                    costs[i][j] += costs[i - 1][sec_min_color]
                else:
                    costs[i][j] += costs[i - 1][min_color]
        return min(costs[-1])

            