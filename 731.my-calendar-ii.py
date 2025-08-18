#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for os, oe in self.overlaps:
            if startTime < oe and endTime > os:
                return False
        for bs, be in self.booked:
            if startTime < be and endTime > bs:
                self.overlaps.append((max(startTime, bs), min(endTime, be)))
        self.booked.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

