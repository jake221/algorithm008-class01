# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            res.extend(self._threeSum(nums[i+1:], target - nums[i], nums[i]))
        return res


    def _threeSum(self, nums, target, tmp):
        # nums.sort()
        # 判断a + b + c + d = target
        # 如果
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            # nums[i]为a; 现在是通过两端夹逼法确定b, c, d
            while left < right:
                if nums[left] + nums[right] < target - nums[i]:
                    left += 1
                elif nums[left] + nums[right] > target - nums[i]:
                    right -= 1
                else:
                    res.add((tmp, nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return list(map(list, res))

solver = Solution()
print(solver.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9))



