# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 # insert position
        for r in range(len(nums)):
            if l < 2 or nums[r] != nums[l-2]:
                nums[l] = nums[r]
                l += 1
        return l
