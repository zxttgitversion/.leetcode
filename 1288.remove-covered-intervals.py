#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        cnt = 0
        end = 0

        for start, end in intervals:
            if end > curr_end:
                cnt += 1
                curr_end = end
                
        return cnt

# @lc code=end

