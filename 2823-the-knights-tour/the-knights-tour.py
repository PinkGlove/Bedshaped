class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, k):
            if k == m * n:
                return True
            for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == -1:
                    board[nx][ny] = k
                    if dfs(nx, ny, k + 1):
                        return True
                    board[nx][ny] = -1
            return False
        
        board[r][c] = 0
        dfs(r, c, 1)
        return board