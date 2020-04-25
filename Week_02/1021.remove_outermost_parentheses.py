# -*- coding: utf-8 -*-

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num = 0
        idxes = [0]
        tmp_str = ''
        for idx, c in enumerate(S):
            if c == '(':
                num += 1
            else:
                num -= 1
            if num == 0:
                idxes.append(idx)
                tmp_str += S[idxes[0]+1:idxes[1]]
                idxes = []
                idxes.append(idx+1)
        return tmp_str

sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))







