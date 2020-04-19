# -*- coding: utf-8 -*-
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1
        tmp_lst = [c for c in S]
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                tmp_lst[i], tmp_lst[j] = tmp_lst[j], tmp_lst[i]
                i += 1
                j -= 1
        res = ''.join(tmp_lst)
        return res