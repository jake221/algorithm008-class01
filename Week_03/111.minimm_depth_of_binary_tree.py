# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def minDepth(self, root) -> int:
        # root两个节点均为空时返回1
        # root两个节点有一个为空时，返回不为空的节点深度
        # root两个节点均不为空时时，返回
        # TODO: 逻辑还可以合并优化
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return min(left, right) + 1
        return (left + 1) if left else (right + 1)