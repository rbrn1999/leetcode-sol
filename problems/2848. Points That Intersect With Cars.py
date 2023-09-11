# link: https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort()
        points = 0
        start = nums[0][0]
        end = nums[0][0]
        for s, e in nums:
            if s > end:
                points += end - start + 1
                start = s
                end = e
            else:
                end = max(end, e)
        
        points += end - start + 1
        return points

# Line Sweep
class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        vector = [0] * (100+1+1)
        for start, end in nums:
            vector[start] += 1
            vector[end+1] -= 1 # include "end" in the segment (e.x. [1, 3] -> [1, 1, 1, 0 ...])
        
        state = 0 # number of segments at this point
        answer = 0
        for i in range(101):
            state += vector[i]
            if state > 0:
                answer += 1
        
        return answer
        