# -*- coding: utf-8 -*-
__author__ = 'jack'

from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        # 每个字符排序构造dic
        dic = {}
        res = []
        for s in strs:
            word_gram = ''.join(sorted(s))
            dic.setdefault(word_gram, []).append(s)
            # if word_gram not in dic.keys():
            #     dic[word_gram] = [s]
            # else:
            #     dic[word_gram].append(s)
        for key in dic.keys():
            res.append(dic[key])
        return res


solver = Solution()
print(solver.groupAnagrams(["eat", "tea", "teaa", "tan", "ate", "nat", "bat"]))
