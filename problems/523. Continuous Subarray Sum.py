# link: https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_sum_index = {} # store sum(0...i) % k
        prev = 0
        prefix_sum_index[0] = 0

        for i, num in enumerate(nums):
            cur_sum = (prev + num) % k
            if cur_sum in prefix_sum_index:
                if i - prefix_sum_index[cur_sum] + 1 >= 2:
                    return True
                else:
                    continue

            prefix_sum_index[cur_sum] = i + 1
            prev = cur_sum

        return False
