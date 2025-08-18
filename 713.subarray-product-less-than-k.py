#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0  # 所有正整数乘积都 ≥ 1，无法满足
        
        product = 1
        left, right = 0, 0
        cnt = 0

        while right < len(nums):
            product *= nums[right]
            right += 1

            while product >= k:
                product //= nums[left]
                left += 1

            cnt += (right - left)

        return cnt
# @lc code=end

