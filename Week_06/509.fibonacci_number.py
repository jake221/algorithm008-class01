# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def fib(self, N: int) -> int:
        # 1. dp
        res = {}
        for i in range(N + 1):
            if i <= 1:
                res[i] = i
            else:
                res[i] = res[i - 1] + res[i - 2]
        return res[N]

    def fib2(self, N: int) -> int:
        # 2. memory search
        mem = [0 for i in range(31)]
        if N <= 1:
            return N
        else:
            mem[N] = self.fib2(N - 1) + self.fib2(N - 2)
        return mem[N]


solver = Solution()
print(solver.fib2(1))
print(solver.fib2(2))
print(solver.fib2(3))
print(solver.fib2(4))
