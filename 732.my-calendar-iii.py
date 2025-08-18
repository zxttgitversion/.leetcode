#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start
from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.delta = defaultdict(int)
        self.max_active = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] += 1
        self.delta[endTime] -= 1

        active = 0
        for time in sorted(self.delta):
            active += self.delta[time]
            self.max_active = max(self.max_active, active)
        return self.max_active


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

