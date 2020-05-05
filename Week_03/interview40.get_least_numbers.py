# -*- coding: utf-8 -*-
import heapq

class Solution:
    def getLeastNumbers(self, arr, k):
        # 1. sort后取前k个
        # 2. 快排
        # 3. 大顶堆
        # 3. 大顶堆的思路是前k个元素进大顶堆，然后遍历数组剩下的元素，
        # 如果当前元素小于堆顶元素，则弹出堆顶元素，再插入当前遍历到的数
        # 最后将大根堆里的数存入数组即可并维护这个k个元素的小顶堆
        # 注意python默认的堆是小顶堆，存入取出皆取反即可
        if k == 0:
            return list()
        hq = [-x for x in arr[:k]]
        heapq.heapify(hq)

        for i in arr[k:]:
            if -hq[0] > i:
                heapq.heapreplace(hq, -i)
        return [-x for x in hq]