# link: https://leetcode.com/problems/jump-game/

'''
Greedy, bottom-up
Time Complexity: O(n)
Space Complexity: O(1)
'''
# update shorter solution (2022/12/26)
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        reach = 0
        for i in range(n):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
            if reach >= n-1:
                return True
        
        return True


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n-1:
            longestReach = i
            distance = 0
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    return True
                if nums[i+j] + j >= distance:
                    longestReach = i + j
                    distance = nums[i+j] + j
            if i == longestReach:
                return False
            else:
                i = longestReach
        
        return True

'''
Dynamic Programming, top-bottom
Time Complexity: O(n)
Space Complexity: O(1)
link: https://youtu.be/Yan0cv2cLy8
'''

'''
Dynamic Programming, bottom-up
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [0] * len(nums)

        dp[0] = 1
        i = 0
        while i < len(nums):
            if dp[i] == 0:
                return False
            dp[i+1:i+nums[i]+1] = [1] * nums[i]
            i += 1
        
        return True if dp[-1] == 1 else False
