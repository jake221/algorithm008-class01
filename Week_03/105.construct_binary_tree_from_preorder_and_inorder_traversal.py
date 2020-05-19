# -*- coding: utf-8 -*-
__author__ = 'jack'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):

        # 基于preorder的第一个节点找到根节点
        root = TreeNode(preorder[0])
        # 然后基于根节点的位置在inorder中定位左子树和右子树
        root_idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[1 + root_idx:], inorder[1 + root_idx:])
        return root
