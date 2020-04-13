# -*- coding: utf-8 -*-


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 逆序法
        if len(nums) <= 1:
            return
        else:
            k = k % len(nums)
            self._reverse(nums, 0, len(nums) - 1)
            self._reverse(nums, 0, k - 1)
            self._reverse(nums, k, len(nums) - 1)

    @staticmethod
    def _reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    sol.rotate(nums2, 3)
    sol.rotate(nums3, 3)
    assert nums1 == [2, 1]
    assert nums2 == [1]
    assert nums3 == [5, 6, 7, 1, 2, 3, 4]
