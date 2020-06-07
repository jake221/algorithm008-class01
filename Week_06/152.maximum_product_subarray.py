# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp
        max_product = maximum = minimum = nums[0]
        for n in nums[1:]:
            # 保存max和min两个数值
            maximum, minimum = max(n, maximum * n, minimum * n), min(n, maximum * n, minimum * n)
            max_product = max(maximum, max_product)
        return max_product