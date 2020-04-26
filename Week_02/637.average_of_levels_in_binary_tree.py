# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def averageOfLevels(self, root):
        res = []
        res = self.helper(root, 0, res)
        return [sum(l) / len(l) for l in res]

    def helper(self, root, level, traverse):
        if root:
            if len(traverse) == level:
                traverse.append([])
            traverse[level].append(root.val)
            if root.left:
                self.helper(root.left, level + 1, traverse)
            if root.right:
                self.helper(root.right, level + 1, traverse)
        return traverse