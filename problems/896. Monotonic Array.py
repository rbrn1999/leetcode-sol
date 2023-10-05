# link: https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        state = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if state == -1:
                    return False
                else:
                    state = 1
            elif nums[i] < nums[i-1]:
                if state == 1:
                    return False
                else:
                    state = -1
            else:
                pass
        
        return True