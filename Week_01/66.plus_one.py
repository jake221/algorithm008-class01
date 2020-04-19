# -*- coding: utf-8 -*-
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 暴力法
        tmp_str = str(int(''.join(list(map(str, digits)))) + 1)
        return [int(c) for c in tmp_str]
