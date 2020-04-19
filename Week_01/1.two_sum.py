# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic.keys():
                dic[nums[i]] = i
            else:
                return [i, dic[target - nums[i]]]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
