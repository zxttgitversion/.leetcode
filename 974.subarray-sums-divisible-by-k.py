#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)  #{remainder: occurances}
        cnt[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            m = prefix % k
            res += cnt[m]
            cnt[m] += 1
        return res
# @lc code=end

