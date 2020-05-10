# -*- coding: utf-8 -*-
__author__ = 'jack'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 1. 按照二叉树的最近公共祖先去做
        # if (root is None) or (root == p) or (root == q):
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     return root
        # return left if left else right

        # 2. 利用二叉搜索树的性质
        if (root is None) or (root == p) or (root == q):
            return root
        # p, q分别为root的左右子树上的节点
        if p.val < root.val and root.val < q.val:
            return root
        if p.val > root.val and root.val > q.val:
            return root
        # p, q均小于root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p,q均大于root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)