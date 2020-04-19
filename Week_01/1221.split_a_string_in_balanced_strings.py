# -*- coding: utf-8 -*-
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num, res = 0, 0
        for c in s:
            if c == 'R':
                num += 1
            else:
                num -= 1
            if num == 0:
                res += 1
        return res