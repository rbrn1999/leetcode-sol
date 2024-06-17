# link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# Sorting
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        increments = 0
        non_unique_count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                non_unique_count += 1
            else:
                slots = min(non_unique_count, nums[i]-nums[i-1]-1)
                increments += ((non_unique_count - slots + 1) + non_unique_count) * slots // 2
                non_unique_count -= slots

                increments += non_unique_count


        increments += (1 + non_unique_count) * non_unique_count // 2 # sum of [1...non_unique_count]

        return increments

# Counting Sort
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        max_num = max(nums)
        counts = [0] * (max_num + 1)
        for num in nums:
            counts[num] += 1

        non_unique = 0
        increments = 0

        for num in range(max_num+1):
            increments += non_unique
            non_unique = max(non_unique + counts[num] - 1, 0)

        increments += (1 + non_unique) * non_unique // 2

        return increments
