# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        valueIndex = {}
        for ind, num in enumerate(numbers):
            if target-num in valueIndex.keys():
                return [valueIndex[target-num], ind+1]
            else:
                valueIndex[num] = ind+1
