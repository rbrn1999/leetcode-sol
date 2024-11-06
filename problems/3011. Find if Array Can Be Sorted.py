# link: https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cur_bits = nums[0].bit_count()
        cur_max = nums[0]
        prev_max = -float('inf')

        for num in nums:
            if num.bit_count() == cur_bits:
                cur_max = max(cur_max, num)
            else:
                prev_max = cur_max
                cur_max = num
                cur_bits = num.bit_count()

            if num < prev_max:
                return False

        return True