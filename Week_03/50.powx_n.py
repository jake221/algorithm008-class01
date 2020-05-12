# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. x ** n
        # 2. divide and conquer
        # 3. brute force
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        return half * half * x if (n % 2) else (half * half)


solver = Solution()
print(solver.myPow(2, 10))
