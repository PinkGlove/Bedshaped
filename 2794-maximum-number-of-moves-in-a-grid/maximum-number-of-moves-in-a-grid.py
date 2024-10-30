class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        steps = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for col in range(1, len(grid[0])):
            walkable = False
            for row in range(len(grid)):
                curr = 0
                if grid[row][col] > grid[row][col - 1]:
                    if col == 1 or (col > 1 and steps[row][col - 1] != 0):
                        curr = max(curr, steps[row][col - 1] + 1)
                if row - 1 >= 0 and grid[row][col] > grid[row - 1][col - 1]:
                    if col == 1 or (col > 1 and steps[row - 1][col - 1] != 0):
                        curr = max(curr, steps[row - 1][col - 1] + 1)
                if row + 1 < len(grid) and grid[row][col] > grid[row + 1][col - 1]:
                    if col == 1 or (col > 1 and steps[row + 1][col - 1] != 0):
                        curr = max(curr, steps[row + 1][col - 1] + 1)
                steps[row][col] = curr
                if curr != 0:
                    walkable = True
            if not walkable:
                return max([steps[row][col - 1] for row in range(len(grid))])
        return max([steps[row][-1] for row in range(len(grid))])