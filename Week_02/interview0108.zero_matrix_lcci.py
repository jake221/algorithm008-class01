# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def setZeroes(self, matrix) -> None:
        zero_entries = []
        # 第一次遍历，记录哪些元素为零
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_entries.append((r, c))

        # 行转零
        for r, _ in zero_entries:
            matrix[r] = [0] * len(matrix[0])

        # 列转零
        for r in range(len(matrix)):
            for _, c in zero_entries:
                matrix[r][c] = 0

        return matrix

solver = Solution()
print(solver.setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]))
