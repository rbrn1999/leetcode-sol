# link: https://leetcode.com/problems/design-underground-system/

from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        # key: id, value: (stationName, t)
        self.customerIn = {}

        # key: (start, destination), value: (totalTime, Count)
        self.travelTimes = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.customerIn:
            return
        self.customerIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customerIn:
            return
        startStation, startTime = self.customerIn[id]
        del self.customerIn[id]
        self.travelTimes[(startStation, stationName)][0] += t - startTime
        self.travelTimes[(startStation, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.travelTimes[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)