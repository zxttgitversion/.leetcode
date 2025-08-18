#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left, right = 0, 0
        window_sum = 0
        max_avg = float('-inf')

        while right < n:
            window_sum += nums[right]
            right += 1

            if right - left == k:
                max_avg = max(max_avg, window_sum / k)
                window_sum -= nums[left]
                left += 1 

        return max_avg
# @lc code=end

