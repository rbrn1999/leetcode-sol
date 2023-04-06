# link: https://leetcode.com/problems/minimize-maximum-of-array/

# binary search 
# time complexity: O(n*log(max(nums)-avg(nums)))
import math
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        def isValid(minVal: int) -> bool:
            space = 0
            for num in nums:
                space += (minVal - num)
                if space < 0:
                    return False
            return True

        low = math.ceil(sum(nums)//len(nums))
        high = max(nums)

        while low < high:
            print(low, high)
            mid = low + (high-low) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1

        return low

# prefix sum + greedy
# time complexity O(n)
import math
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        prefixSum = 0
        minVal = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            minVal = max(minVal, math.ceil(prefixSum / (i+1)))
        
        return minVal
