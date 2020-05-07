# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def isValidBST(self, root) -> bool:
        # 1. 中序遍历（两种，更高效的是只比较前继节点）
        # 2. 递归
        in_order_lst = self.in_order(root)
        return in_order_lst == list(sorted(set(in_order_lst)))

    def in_order(self, root):
        if root is None:
            return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)