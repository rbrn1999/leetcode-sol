# link: https://leetcode.com/problems/car-pooling/

# Heap, Sorting
import heapq
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        drop = [] # (pos, people count)
        trips.sort(key=lambda x: (x[1], x[2]))

        for passengers, start, end in trips:
            while drop and drop[0][0] <= start:
                _, dropped = heapq.heappop(drop)
                capacity += dropped
            
            if passengers > capacity:
                return False
            else:
                capacity -= passengers
            
            heapq.heappush(drop, (end, passengers))
        
        return True

# Bucket Sort, Scanning
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        minStart = float('inf')
        maxEnd = 0

        for _, start, end in trips:
            minStart = min(minStart, start)
            maxEnd = max(maxEnd, end)
        
        passengers = [0] * (maxEnd - minStart + 1)

        for passenger_count, start, end in trips:
            passengers[start-minStart] += passenger_count
            passengers[end-minStart] -= passenger_count

        for passenger_count in passengers:
            capacity -= passenger_count
            if capacity < 0:
                return False
        
        return True