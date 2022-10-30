# link: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        indexes = list(range(len(plantTime)))
        indexes.sort(key=lambda i: -growTime[i])

        res = 0
        curTime = 0
        for i in indexes:
            curTime += plantTime[i]
            res = max(res, curTime + growTime[i])
        return res

