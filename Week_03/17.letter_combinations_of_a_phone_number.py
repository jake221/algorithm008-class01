# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def letterCombinations(self, digits: str):
        # TODO: 有效性判断
        res = []

        dic = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

        self._generate(0, digits, "", res, dic)
        return res

    def _generate(self, index: int, digits: str, s: str, res: list, dic: dict):
        # terminator
        if (index == len(digits)):
            res.append(s)
            return
        # process current logic: 从当前数字对应的字母中挑选一个
        tmp = dic[digits[index]]
        for c in tmp:
            self._generate(index + 1, digits, s + c, res, dic)


solver = Solution()
print(solver.letterCombinations("23"))
