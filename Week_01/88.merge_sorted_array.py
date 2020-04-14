# -*- coding: utf-8 -*-
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 双指针法
        # 使用copy时，后面对tmp_nums操作不会改变nums
        tmp_nums = nums1.copy()
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp_nums[k] = nums1[i]
                i += 1
            else:
                tmp_nums[k] = nums2[j]
                j += 1
            k += 1
        if i == m:
            tmp_nums[k:] = nums2[j:]
        else:
            tmp_nums[k:] = nums1[i:m]
        nums1[:] = tmp_nums


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3, 4, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
