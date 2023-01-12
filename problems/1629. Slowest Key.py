# link: https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        result = (0, 'a')
        for i in range(len(releaseTimes)):
            result = max(result, (releaseTimes[i] - prev, keysPressed[i]))
            prev = releaseTimes[i]

        return result[1]

