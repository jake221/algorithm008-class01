# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp方程: dp[i, j] = min(dp[i+1, j], dp[i+1, j+1]) + v[i, j]
        dp = triangle
        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                dp[r][c] += min(dp[r+1][c], dp[r+1][c+1])
        return dp[0][0]