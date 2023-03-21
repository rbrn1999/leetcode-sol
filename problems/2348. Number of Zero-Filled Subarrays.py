# link: https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def countSubarray(length: int) -> int:
            count = 0
            for i in range(length):
                count += length-i # array length: i+1, starting indexs of array: [0 to (length-1)-(i+1)+1]
            return count

        subarray_count = 0
        zero_count = 0
        nums.append(1)
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                subarray_count += countSubarray(zero_count)
                zero_count = 0

        return subarray_count

