# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def postorder(self, root):
        res = []
        return self.helper(root, res)


    def helper(self, root, traverse):
        # children, root
        if root:
            if root.children:
                for child in root.children:
                    self.helper(child, traverse)
            traverse.append(root.val)

        return traverse
