# -*- coding: utf-8 -*-
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法
        # 容器可容纳的水由最短的边决定
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            # move the short side to the middle
            if height[left] <= height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
        return max_area