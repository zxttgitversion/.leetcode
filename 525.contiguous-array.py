#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start

"""
see 1, prefixsum += 1; see 0,  prefixsum -= 1

 if in idx from i to j - 1, there are same nums of 0 and 1
 then prefix[j] - prefix[i] = sum(nums[i] to nums[j - 1]) = 0
 =>   prefix[j] = prefix[i] 

 len = j - i
"""


from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map = {0 : -1} # {prefix : index}
        prefix = 0
        max_len = 0

        for idx, num in enumerate(nums):
            prefix += 1 if num == 1 else -1

            if prefix in prefix_map:
                curr_len = idx - prefix_map[prefix]
                if max_len < curr_len:
                    max_len = curr_len
            else:
                prefix_map[prefix] = idx

        return max_len

# @lc code=end

