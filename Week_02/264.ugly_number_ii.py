# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 1
        i = 2
        while count < n:
            if (i % 2 == 0) | (i % 3 == 0) | (i % 5 == 0):
                print(i)
                count += 1
            i += 1

        return i - 1

solver = Solution()
print(solver.nthUglyNumber(11))