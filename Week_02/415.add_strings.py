# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def addStrings(self, num1, num2):
        # 指针
        i = len(num1) - 1
        j = len(num2) - 1
        tmp_sum = 0
        while (i >= 0) and (j >= 0):
            tmp_sum += (int(num1[i]) + int(num2[j])) * (10 ** (len(num1) - i - 1))
            i -= 1
            j -= 1
        while i >= 0:
            tmp_sum += (int(num1[i])) * (10 ** (len(num1) - i - 1))
            i -= 1
        while j >= 0:
            tmp_sum += (int(num2[j])) * (10 ** (len(num2) - j - 1))
            j -= 1
        return tmp_sum


solver = Solution()
print(solver.addStrings('3322', '45'))
