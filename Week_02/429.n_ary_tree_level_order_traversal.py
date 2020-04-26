# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def levelOrder(self, root):
        res = []
        return self.helper(root, 0, res)

    def helper(self, root, level, traverse):
        if root:
            if len(traverse) == level:
                traverse.append([])
            traverse[level].append(root.val)
            if root.children:
                for child in root.children:
                    self.helper(child, level + 1, traverse)
        return traverse
