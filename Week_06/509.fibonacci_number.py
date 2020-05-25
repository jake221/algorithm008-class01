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
        self.mem = [-1 for _ in range(N + 1)]
        return self._helper(N)

    def _helper(self, n):
        if n <= 1:
            return n
        if self.mem[n] == -1:
            self.mem[n] = self._helper(n - 1) + self._helper(n - 2)
        return self.mem[n]


solver = Solution()
print(solver.fib2(1))
print(solver.fib2(2))
print(solver.fib2(3))
print(solver.fib2(4))
