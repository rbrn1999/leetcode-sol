# link: https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = ((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])) if coordinates[0][0] != coordinates[1][0] else float('inf')
        for i in range(1, len(coordinates)-1):
            new_m = ((coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0])) if coordinates[i][0] != coordinates[i+1][0] else float('inf')
            if m != new_m:
                return False
        return True
    