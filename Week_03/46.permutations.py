# -*- coding: utf-8 -*-
__author__ = 'jack'

from itertools import permutations


class Solution:
    def permute(self, nums):
        return [list(r) for r in permutations(nums)]


solver = Solution()
print(solver.permute([1, 2, 3]))
