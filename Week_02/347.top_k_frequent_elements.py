# -*- coding: utf-8 -*-
__author__ = 'jack'

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        nums_dic = sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)
        print(nums_dic)
        res = []
        for idx, key in enumerate(nums_dic):
            if idx > k -1:
                break
            res.append(key[0])
        return res

solver = Solution()
print(solver.topKFrequent([4,1,-1,2,-1,2,3], 2))