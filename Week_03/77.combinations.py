# -*- coding: utf-8 -*-
__author__ = 'jack'

# https://leetcode-cn.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int):
        res = []
        self._dfs(res, [], 0, [i for i in range(1, n + 1)], k)
        return res

    def _dfs(self, res, path, index, nums, k):
        # terminator
        if not k:
            res.append(path)
            return
        # process the current logic
        for i in range(index, len(nums)):
            self._dfs(res, path + [nums[i]], i + 1, nums, k - 1)


solver = Solution()
print(solver.combine(4, 2))
