# -*- coding: utf-8 -*-
class Solution:
    def sortedSquares(self, A):
        # 1. 平方后排序
        # square_list = [e**2 for e in A]
        # square_list.sort()
        # return square_list

        # 2. 双指针
        if len(A) == 1:
            return [A[0] ** 2]
        i = 0
        while A[i] < 0:
            i += 1
        j = i - 1
        square_list = []
        while i < len(A) and j >= 0:
            if A[i] ** 2 <= A[j] ** 2:
                square_list.append(A[i]**2)
                i += 1
            else:
                square_list.append(A[j]**2)
                j -= 1
        print(square_list)
        while j >= 0:
            square_list.append(A[j] ** 2)
            j -= 1
        while i < len(A):
            square_list.append(A[i] ** 2)
            i += 1
        return square_list

sol = Solution()
print(sol.sortedSquares([-4,-3,0,1,2]))