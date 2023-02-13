# link: https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        total = sum(nums)
        r_nums = [[], []]

        for num in nums:
            if num % 3 != 0:
                r_ind = num % 3 - 1
                if len(r_nums[r_ind]) < 2:
                    r_nums[r_ind].append(num)
                elif r_nums[r_ind][1] > num:
                    r_nums[r_ind][1] = num
                else:
                    continue
                r_nums[r_ind].sort()

        result = 0
        if total % 3 == 0:
            result = total
        else:
            r_ind = total % 3 - 1
            if len(r_nums[r_ind]) > 0:
                result = total - r_nums[r_ind][0]
            if len(r_nums[(r_ind+1)%2]) == 2:
                result = max(result, total - sum(r_nums[(r_ind+1)%2]))
            
        return result
            

