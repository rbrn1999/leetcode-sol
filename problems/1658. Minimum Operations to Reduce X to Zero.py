# link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero
# solution: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2136570

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        left = curSum = 0
        maxLen = -1
        target = sum(nums) - x

        for right in range(len(nums)):
            curSum += nums[right]
            while left <= right and curSum > target:
                curSum -= nums[left]
                left += 1
            if curSum == target:
                maxLen = max(maxLen, right - left + 1)
        
        return len(nums) - maxLen if maxLen != -1 else -1

    

nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365



print(Solution().minOperations(nums, x))
        


# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         if sum(nums) < x:
#             return -1
        
#         MAX = 100001
#         MIN = MAX
#         def dfs(start, end, x, steps):
#             nonlocal nums, MAX, MIN
#             if steps >= MIN:
#                 return
            
#             if x == 0:
#                 MIN = min(MIN, steps)
#             elif x > 0:
#                 dfs(start+1, end, x-nums[start], steps+1)
#                 dfs(start, end-1, x-nums[end], steps+1)
        
#         dfs(0, len(nums)-1, x, 0)
#         return MIN if MIN < MAX else -1
        