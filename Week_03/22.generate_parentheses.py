# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self._generate(0, 0, n, "", res)
        return res

    def _generate(self, left: int, right: int, num_par: int, s: str, res: list):
        if (left == num_par) and (right == num_par):
            res.append(s)
        # 添加左括号的条件：左括号个数小于num_par
        if left < num_par:
            self._generate(left + 1, right, num_par, s + "(", res)
        # 添加右括号的条件：右括号的个数小于
        if right < left:
            self._generate(left, right + 1, num_par, s + ")", res)


solver = Solution()
print(solver.generateParenthesis(3))
