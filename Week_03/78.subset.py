# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._generate(res, [], nums, 0)
        return res

    def _generate(self, res: List[List[int]], tmp: List[int], nums: List[int], index: int):
        # terminator
        if index == len(nums):
            res.append(tmp)
            return

        # process the current logic
        self._generate(res, tmp.copy(), nums, index + 1)  # not pick the number

        tmp.append(nums[index])
        self._generate(res, tmp.copy(), nums, index + 1)  # pick the number