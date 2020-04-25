# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': "(",
               "]": "[",
               "}": "{"}
        stack = ["?"]
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif dic[c] != stack.pop():
                return False
        return True if len(stack) == 1 else False



