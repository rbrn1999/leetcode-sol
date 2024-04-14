# link: https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        t = 0
        for i in range(k+1):
            t += min(tickets[i], tickets[k])
        
        for i in range(k+1, len(tickets)):
            t += min(tickets[i], tickets[k]-1)
        
        return t