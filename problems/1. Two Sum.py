# link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, num in enumerate(nums):
            if target-num not in hashMap.keys():
                hashMap[num] = i
            else:
                return [hashMap[target-num], i]
        return [-1, -1] # no matches