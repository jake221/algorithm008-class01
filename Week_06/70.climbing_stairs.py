# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. recursion (time exceed)
        # 2. memory search
        # 3. dynamic programming
        ways = {}
        for i in range(1, n+1):
            if i <= 2:
                ways[i] = i
            else:
                ways[i] = ways[i-1] + ways[i-2]
        return ways[n]