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
            if root.left:
                self.helper(root.left, level + 1, traverse)
            if root.right:
                self.helper(root.right, level + 1, traverse)
        return traverse
