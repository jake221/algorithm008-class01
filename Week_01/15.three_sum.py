# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def threeSum(self, nums):
        # sort and then i, j
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            if i > 0 and (nums[i] == nums[i - 1]):
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < - nums[i]:
                    left += 1
                elif nums[left] + nums[right] > - nums[i]:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return list(map(list, res))


solver = Solution()
print(solver.threeSum([-1, 0, 1, 2, -1, -4]))
