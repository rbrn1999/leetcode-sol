# link: https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)

        rooms = 0
        max_rooms = 0
        i, j = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        
        return max_rooms