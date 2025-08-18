#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        curr_sum = 0
        freq = Counter()
        ans = 0

        while right < len(nums):
            x = nums[right]
            curr_sum += x
            freq[x] += 1
            right += 1

            if right - left > k:
                y = nums[left]
                curr_sum -= y
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                left += 1

            if right - left == k and len(freq) == k:
                ans = max(ans, curr_sum)

        return ans

# @lc code=end

