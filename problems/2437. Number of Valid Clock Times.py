# link: https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        count = 1
        if time[0] == '?' and time[1] == '?':
            count *= 24
        elif time[0] == '?':
            count *= 2 + int(int(time[1]) <= 3)
        elif time[1] == '?':
            count *= 4 + 6 * int(time[0] != '2')
        
        if time[3] == '?':
            count *= 6
        if time[4] == '?':
            count *= 10
        
        return count