# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def canJump(self, nums: list) -> bool:
        # greedy(backward)
        reach = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= reach:
                reach = i
        return reach == 0