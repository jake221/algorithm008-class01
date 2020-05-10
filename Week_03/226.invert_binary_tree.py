# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def invertTree(self, root):
        # recursion
        # TODO: use stack (iteration to save time)
        if root is None:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root