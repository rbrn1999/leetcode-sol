# link: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

# partial sort
import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        minHeap = [num for num in nums[:4]]
        maxHeap = [-num for num in nums[:4]]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)

        for num in nums[4:]:
            heapq.heappushpop(minHeap, num)
            heapq.heappushpop(maxHeap, -num)

        largest = sorted([num for num in minHeap], reverse=True)
        smallest = sorted(-num for num in maxHeap)
        result = largest[0] - smallest[0]
        
        for i in range(4):
            result = min(result, largest[3-i] - smallest[i])

        return result
        

# built-in
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        largest = sorted(heapq.nlargest(4, nums), reverse=True)
        smallest = sorted(heapq.nsmallest(4, nums))
        result = largest[0] - smallest[0]
        
        for i in range(4):
            result = min(result, largest[3-i] - smallest[i])

        return result
        