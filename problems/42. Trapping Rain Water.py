# link: https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        maxLeft = maxRight = float('-inf')

        while left <= right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
                right -= 1

        return water

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))