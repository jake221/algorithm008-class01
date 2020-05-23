# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        if bills[0] != 5:
            return False
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            elif ten > 0:   # 后面两种情况是找零15元的情况
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True