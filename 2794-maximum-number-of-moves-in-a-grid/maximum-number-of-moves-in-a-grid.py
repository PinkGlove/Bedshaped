class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirs = [-1, 0, 1]

        def dfs(row, col, grid, dp):
            M, N = len(grid), len(grid[0])
            if dp[row][col] != -1:
                return dp[row][col]
            max_moves = 0
            for d in dirs:
                next_row, next_col = row + d, col + 1
                if 0 <= next_row < M and 0 <= next_col < N and grid[row][col] < grid[next_row][next_col]:
                    max_moves = max(max_moves, 1 + dfs(next_row, next_col, grid, dp))
            dp[row][col] = max_moves
            return max_moves
        
        M, N = len(grid), len(grid[0])
        dp = [[-1] * N for _ in range(M)]
        max_moves = 0
        for i in range(M):
            moves_required = dfs(i, 0, grid, dp)
            max_moves = max(max_moves, moves_required)
        return max_moves