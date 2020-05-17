# -*- coding: utf-8 -*-
__author__ = 'jack'

from itertools import permutations


class Solution:
    def permuteUnique(self, nums):
        res = set()
        for r in permutations(nums):
            res.add(r)
        return [list(r) for r in res]


solver = Solution()
print(solver.permuteUnique([1, 1, 2]))
