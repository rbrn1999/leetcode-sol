# link: https://leetcode.com/problems/construct-target-array-with-multiple-sums/
# solution: https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/

import heapq
class Solution:
    def isPossible(self, target: list[int]) -> bool:
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)
        
        # for each iteration 
        
        # backtracking
        while True:
            curTarget = -heapq.heappop(target)
            total -= curTarget
            
            if curTarget == 1 or total == 1:
            # array back to state [1]*n || TODO: figure this out
                return True            
            if total > curTarget or total == 0 or curTarget % total == 0:
            # total (sum) is too big to make up curTarget || total is 0, can't reduce anything || curTarget can't be reduced under '1' TODO: figure this out
                return False
            
            reducedTarget = curTarget % total
            total += reducedTarget
            
            heapq.heappush(target, -reducedTarget)

print(Solution().isPossible([1,3]))