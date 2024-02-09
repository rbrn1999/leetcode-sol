# link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(0, n, 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                res.append(nums[i:i+3])
        
        return res