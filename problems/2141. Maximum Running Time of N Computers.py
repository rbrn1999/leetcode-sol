# link: https://leetcode.com/problems/maximum-running-time-of-n-computers/

# Approach 1
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        batteries.sort()
        extra = sum(batteries[:m-n])
        using = batteries[m-n:]
        for i in range(n-1): 
            # try distributing extra enery to batteries with lower energy
            if extra // (i+1) < using[i+1] - using[i]: # extra not enough to distribute to match the using[i+1]
                return using[i] + extra // (i+1)
            else:
                # with extra, make "using" 0~i match the level of using[i+1] 
                extra -= (i+1) * (using[i+1] - using[i])
        
        # all batteries at the level of using[n-1]
        # distribute extra to the n using batteries
        return using[-1] + extra // n

# Binary Search
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = 0
        high = sum(batteries) // n

        def canRun(runTime: int) -> bool:
            energyNeeded = runTime * n
            for battery in batteries:
                energyNeeded -= min(battery, runTime) # a battery can utilize at most "runtime" engery
                if energyNeeded <= 0:
                    return True
            return False

        while low + 1 < high:
            mid = low + (high - low) // 2
            if canRun(mid):
                low = mid
            else:
                high = mid - 1
        
        return high if canRun(high) else low