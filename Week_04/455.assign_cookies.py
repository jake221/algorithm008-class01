# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def findContentChildren(self, g, s) -> int:
        # greedy
        res = 0

        g.sort()
        s.sort()

        # 双指针
        i = 0
        j = 0
        while (i < len(g)) and (j < len(s)):
            # 如果胃口小于等于饼干尺寸则两个指针均右移
            # 否则仅右移饼干尺寸
            if g[i] <= s[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
        return res

