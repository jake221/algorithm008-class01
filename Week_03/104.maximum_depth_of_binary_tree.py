# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def maxDepth(self, root) -> int:
        # recursion: max(left + 1, right + 1)
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1