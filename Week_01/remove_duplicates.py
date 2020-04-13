# -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, nums) -> int:
        # 双指针法；将非重复项移动到左边
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return nums[:i+1]