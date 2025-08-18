#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {} # userid -> (stationName, t)
        self.trip_data = {}     # (startstation, endstation) -> (totaltime, tripcount)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        trip_key = (start_station, stationName)
        trip_time = t - start_time
        if trip_key not in self.trip_data:
            self.trip_data[trip_key] = [0, 0]

        self.trip_data[trip_key][0] += trip_time
        self.trip_data[trip_key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, trip_count = self.trip_data[(startStation, endStation)]
        return total_time/trip_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

