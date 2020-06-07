# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = nums
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + dp[i])

        return dp[-1]