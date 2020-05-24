# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def mySqrt(self, x: int) -> int:
        # 1. binary search
        # 两个问题：mid的计算公式；
        # left = 0
        # right = x
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid > x:
        #         right = mid - 1 # 二分模板
        #     else:
        #         left = mid + 1
        # return right
        # 2. newton
        if x == 0:
            return x

        cur = 1
        while True:
            cur = (cur + x / cur) / 2
            if abs(cur*cur - x) < 1e-6:
                return int(cur)