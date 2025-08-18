#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始：imax/imin 都为 nums[0]，res 为全局最大乘积
        imax = imin = res = nums[0]
        
        # 从第二个元素开始
        for x in nums[1:]:
            # 在更新 imax/imin 前先保存旧值
            prev_max, prev_min = imax, imin
            
            # 计算以 x 结尾的最大/最小乘积
            imax = max(prev_max * x, prev_min * x, x)
            imin = min(prev_max * x, prev_min * x, x)
            
            # 更新全局结果
            res = max(res, imax)
        
        return res

# @lc code=end

