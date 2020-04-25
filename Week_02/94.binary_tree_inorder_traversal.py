# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def inorderTraversal(self, root):
        res = []
        return self.helper(root, res)

    def helper(self, root, traverse):
        if root:
            if root.left:
                self.helper(root.left, traverse)
            traverse.append(root.val)
            if root.right:
                self.helper(root.right, traverse)
        return traverse