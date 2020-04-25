# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def preorder(self, root):
        res = []
        return self.helper(root, res)

    def helper(self, root, traverse):
        if root:
            traverse.append(root.val)
            if root.children:
                for child in root.children:
                    self.helper(child, traverse)
        return traverse