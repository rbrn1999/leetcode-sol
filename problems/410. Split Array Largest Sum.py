# link: https://leetcode.com/problems/split-array-largest-sum/description/
# solution: https://leetcode.com/problems/split-array-largest-sum/solutions/1899144/

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            curSum = 0
            count = 1
            # check the minimum splits there can be with the max sum less or equal to mid
            for num in nums:
                if curSum + num <= mid:
                    curSum += num
                else:
                    curSum = num
                    count += 1
            
            if count > k:
                # can't be split into k portions with all of the sum not being larger than mid
                low = mid + 1
            else:
                # can split into k portions with all the sum being less or equal to mid
                # tighter the upper bound and try to find a smaller answer
                high = mid
        
        return high