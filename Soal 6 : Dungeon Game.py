from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

        for c in range(cols - 2, -1, -1):
            dp[rows - 1][c] = max(1, dp[rows - 1][c + 1] - dungeon[rows - 1][c])

        for r in range(rows - 2, -1, -1):
            dp[r][cols - 1] = max(1, dp[r + 1][cols - 1] - dungeon[r][cols - 1])

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                min_hp_from_next_cell = min(dp[r + 1][c], dp[r][c + 1])
                dp[r][c] = max(1, min_hp_from_next_cell - dungeon[r][c])

        return dp[0][0]
