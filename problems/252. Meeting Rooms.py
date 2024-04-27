# link: https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        prev = -1
        for start, end in sorted(intervals):
            if start < prev:
                return False
            prev = end
        
        return True