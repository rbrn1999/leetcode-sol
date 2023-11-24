# link: https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        t = 0
        accumulate = {'M': 0, 'P': 0, 'G': 0}
        for i in range(len(garbage)):
            s = set(garbage[i])
            t += len(garbage[i])
            for assortment in accumulate:
                if assortment in s:
                    t += accumulate[assortment]
                    accumulate[assortment] = 0
                if i < len(travel):
                    accumulate[assortment] += travel[i]
            
        return t