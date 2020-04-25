# -*- coding: utf-8 -*-
class Solution:
    def maxSlidingWindow(self, nums, k):
        i = 0
        j = k - 1
        tmp_max = []
        while j < len(nums):
            print(j)
            tmp_max.append(max(nums[i:j + 1]))
            i += 1
            j += 1
        return tmp_max


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
