# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 实现一个求平方根的函数

        res = num
        while res * res > num:
            res = (res + num / res) // 2
        return res * res == num