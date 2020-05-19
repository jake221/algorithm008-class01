# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def levelOrder(self, root):
        # 1. dfs
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

    def levelOrder2(self, root):
        # 2. bfs
        if root is None:
            return []
        queue = [root]
        res = []

        # 每一个循环得到一层的结果
        while queue:
            children = []
            tmp_res = []
            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(tmp_res)
            queue = children
        return res
