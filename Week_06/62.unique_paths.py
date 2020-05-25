class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # dp[i][j]表示从[0,0]到[i,j]的路径数
        # 越界的情况也就是i=0或者j=0的情况
        # dp[0][j]对应第一行的情况，也就是从[0,0]到[0,j]的路径数全为1
        # 同上可得dp[i][0]也全为1

        opt = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if (r == 0) or (c == 0):
                    opt[r][c] = 1
                else:
                    opt[r][c] = opt[r-1][c] + opt[r][c-1]
        return opt[m-1][n-1]