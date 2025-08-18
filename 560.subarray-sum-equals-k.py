#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
"""
 assume j > i > 0

prefix[i] = sum(nums[0] to nums[i - 1])
prefix[j] = sum(nums[0] to nums[j - 1])

=> sum(nums[i] to nums[j]) = prefix[j + 1] - prefix[i]

let sum(nums[i] to nums[j]) = k

 then prefix[i] = prefix[j + 1] - k

 we check if there exist prefix[i] = prefix[j + 1] - k 
 and count the existances of prefix[i] = prefix[j + 1] - k 


当我们在遍历到位置 `j` 时，`prefix_sum` 就是当前的 `prefix[j+1]`
若之前某个位置 `i` 的前缀和正好等于 `prefix_sum - k`，那么从 `i` 到 `j` 的子数组和就是 k
"""
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefix_map = {0: 1}
        
        res = 0
        for i in nums:
            prefix += i
            res += prefix_map.get(prefix - k, 0)
            prefix_map[prefix] = prefix_map.get(prefix, 0) + 1

        return res
            

# @lc code=end

