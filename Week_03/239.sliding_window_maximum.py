# -*- coding: utf-8 -*-
__author__ = 'jack'
from collections import deque
# https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)
# keep indexes of good candidates in deque d. The indexes in d are from the current window, they are
# increasing, and their corresponding nums are decreasing. The the first deque element is the index of
# largest window value.
# for each index i
# 1. pop (from the end) indexes of smaller elements
# 2. append the current index
# 3. pop (from the front) the index i - k, if it's still in the deque (it falls out of the window)
# 4. if our window has reached size k, append the current window maximum to the output
class Solution:
    def maxSlidingWindow(self, nums, k):
        # 双端队列
        d = deque()
        res = []
        for i, n in enumerate(nums):
            # 如果双端队列中存在元素且最后一个元素小于当前元素，移除最后一位元素
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i) # 双端队列添加的是滑动窗口的索引
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        return res


solver = Solution()
print(solver.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
