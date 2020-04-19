# -*- coding: utf-8 -*-
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        cols = len(A[0])
        rows = len(A)
        a_trans = [[None] * rows for _ in range(cols)]  # python的特性

        for c in range(cols):
            for r in range(rows):
                a_trans[c][r] = A[r][c]
        return a_trans