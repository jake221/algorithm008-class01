# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount+1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        return dp[-1] if dp[-1] != float('inf') else -1