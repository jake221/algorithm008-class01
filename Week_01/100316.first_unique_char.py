# -*- coding: utf-8 -*-
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if len(s) == 0:
            return " "
        dic = Counter(s)
        for i in s:
            if dic[i] == 1:
                return str(i)
        return " "