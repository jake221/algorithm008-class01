# -*- coding: utf-8 -*-
import sys

__author__ = 'jack'


class Solution:
    def largestRectangleArea(self, heights) -> int:
        # 1. 暴力法
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         min_height = min(heights[i:j + 1])
        #         max_area = max(min_height * (j - i + 1), max_area)
        #
        # return max_area

        # 2. 暴力法优化
        # max_area = 0
        # for i in range(len(heights)):
        #     min_height = heights[0]
        #     for j in range(i + 1, len(heights)):
        #         min_height = min(min_height, heights[j])
        #         max_area = max(min_height * (j - i + 1), max_area)
        # return max_area

        # 3. 问题可以抽取为以第i根柱子为最矮柱子所能延伸的最大面积:O(n^2)
        # max_area = 0
        # for i in range(len(heights)):
        #     height = heights[i]
        #     left = i
        #     right = i
        #     while (left >= 0) and (heights[left] >= height):
        #         left -= 1
        #     while (right <= len(heights) - 1) and (heights[right] >= height):
        #         right += 1
        #     max_area = max(max_area, height * (right - left - 1))
        # return max_area

        # 4. 维护一个栈
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while (stack[-1] != -1) & (heights[stack[-1]] > heights[i]):
                # i 为右边界，栈中下一个元素为其左边界
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area





solver = Solution()
print(solver.largestRectangleArea([2, 1, 5, 6, 2, 3]))
