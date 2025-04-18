"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

from rich import print as rprint

import pprint
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = sum([dp[i][j - 1], dp[i - 1][j]])
        pp.pprint(dp)
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()
    rprint(solution.uniquePaths(m, n))
