# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def preorderTraversal(self, root):
        res = []
        return self.helper(root, res)

    def helper(self, root, traverse):
        if root:
            traverse.append(root.val)
            if root.left:
                self.helper(root.left, traverse)
            if root.right:
                self.helper(root.right, traverse)
        return traverse