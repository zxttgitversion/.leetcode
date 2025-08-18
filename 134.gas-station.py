#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start_index = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        if total_tank >= 0:
            return start_index
        else:
            return -1

# @lc code=end

