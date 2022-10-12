# link: https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            s = set()
            result = set()
            for num in nums:
                if target-num not in s:
                    s.add(num)
                else:
                    result.add(tuple(sorted([num, target-num])))
            return list(result)

        def threeSum(nums, target):
            result = set()
            for i in range(len(nums)):
                twoSumComps = twoSum(nums[i+1:], target-nums[i])
                for comp in twoSumComps:
                    result.add(tuple(sorted([nums[i]]+list(comp))))
            return list(result)

        result = set()
        for i in range(len(nums)):
            threeSumComps = threeSum(nums[i+1:], target-nums[i])
            for comp in threeSumComps:
                result.add(tuple(sorted([nums[i]]+list(comp))))
        return list(result)
