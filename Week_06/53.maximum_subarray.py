# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] += max(dp[i-1], 0)
        return max(dp)