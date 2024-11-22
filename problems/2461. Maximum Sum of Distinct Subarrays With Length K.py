# link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        count = {}
        cur_sum = 0
        max_sum = 0
        repeating_nums = 0
        for num in nums[:k]:
            cur_sum += num
            count[num] = count.get(num, 0) + 1
            if count[num] == 2:
                repeating_nums += 1

        if repeating_nums == 0:
            max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum -= nums[i-k]
            cur_sum += nums[i]

            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] == 2:
                repeating_nums += 1

            count[nums[i-k]] -= 1
            if count[nums[i-k]] == 0:
                del count[nums[i-k]]
            elif count[nums[i-k]] == 1:
                repeating_nums -= 1


            if repeating_nums == 0:
                max_sum = max(max_sum, cur_sum)

        return max_sum
