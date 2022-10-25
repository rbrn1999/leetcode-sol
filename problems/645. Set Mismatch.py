#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
# link: https://leetcode.com/problems/set-mismatch/

# @lc code=start
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        numSet = set(range(1, len(nums)+1))
        result = []
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                result.append(num)
        result.append(numSet.pop())
        return result
# @lc code=end

