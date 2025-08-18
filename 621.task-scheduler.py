#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_freq =max(counter.values())
        # 统计有几种任务出现了 max_freq 次
        max_count = sum(1 for v in counter.values() if v == max_freq)

        min_time = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), min_time)
        
# @lc code=end

