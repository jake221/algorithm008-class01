# -*- coding: utf-8 -*-
__author__ = 'jack'


class Solution:
    def minMutation(self, start, end, bank):
        if not end in bank:
            return -1

        q = [(start, 0)]
        bank = set(bank)  # 转换为set可以降低判断时间为O(1)

        change = {'A': 'CGT',
                  'C': 'AGT',
                  'G': 'ACT',
                  'T': 'ACG'}

        while q:
            node, step = q.pop(0)

            if node == end:
                return step

            # process logic
            for i, c in enumerate(node):
                candidates = change[c]
                for cand in candidates:
                    new = node[:i] + cand + node[i + 1:]
                    if new in bank:  # 该序列在bank中
                        q.append((new, step + 1))
                        bank.remove(new)  # 避免重复遍历
        return -1


solver = Solution()
print(solver.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
