#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        max_len = 0
        left, right = 0, 0

        while right < len(nums):
            x = nums[right]
            cnt[x] += 1
            right += 1

            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left)
            
        return max_len
        
# @lc code=end

