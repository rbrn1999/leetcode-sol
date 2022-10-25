# link: https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = set()
        for i, num in enumerate(nums):
            if i > k:
                numsSet.remove(nums[i-(k+1)])
            if nums[i] in numsSet:
                return True
            numsSet.add(num)
        return False
