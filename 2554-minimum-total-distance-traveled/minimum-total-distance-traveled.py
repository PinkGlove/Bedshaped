class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factory_positions = []
        for x, y in factory:
            for _ in range(y):
                factory_positions.append(x)
        dp = [[-1 for _ in range(len(factory_positions) + 1)] for _ in range(len(robot) + 1)]
        def calculate(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == len(robot):
                return 0
            if j == len(factory_positions):
                return float('inf')
            assign = abs(robot[i] - factory_positions[j]) + calculate(i + 1, j + 1)
            skip = calculate(i, j + 1)
            dp[i][j] = min(assign, skip)
            return dp[i][j]
        return calculate(0, 0)