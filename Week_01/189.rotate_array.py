# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 逆序法
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
