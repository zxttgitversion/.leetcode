#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start 
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        m = len(B)

        total_left = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = total_left - 1
            


# @lc code=end

