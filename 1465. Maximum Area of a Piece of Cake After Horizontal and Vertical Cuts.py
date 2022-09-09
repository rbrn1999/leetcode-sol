# link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        last = 0
        deltaH = 0
        for cut in horizontalCuts:
            deltaH = max(deltaH, cut-last)
            last = cut

        deltaH = max(deltaH, h-last)

        last = 0
        deltaV = 0
        for cut in verticalCuts:
            deltaV = max(deltaV, cut-last)
            last = cut

        print(cut)
        deltaV = max(deltaV, w-last)

        return deltaH * deltaV % int(1E9+7)
