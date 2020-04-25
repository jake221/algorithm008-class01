# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def maxSlidingWindow(self, nums, k):
        # 1. 暴力法
        tmp_lst = []
        for i in range(len(nums) - k + 1):
            tmp_lst.append(max(nums[i:i + k]))
        return tmp_lst
