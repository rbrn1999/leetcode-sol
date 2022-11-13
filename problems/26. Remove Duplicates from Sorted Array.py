# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = len(nums)
        while i < k:
            if nums[i] == nums[i-1]:
                del nums[i]
                k -= 1
            else:
                i += 1

        return k

# solution reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
# 2 pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertInd = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insertInd] = nums[i]
                insertInd += 1
        return insertInd

