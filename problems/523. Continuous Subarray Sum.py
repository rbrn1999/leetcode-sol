# link: https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        accu = [0]
        for i in range(n):
            accu.append(accu[-1] + nums[i])
        '''
        acc[start]%k == acc[end]%k implies (acc[end] - acc[start]) % k == 0
        ->
        find acc[start]%k == acc[end]%k, where start + 2 <= end
        '''
        mod = {}
        for i, val in enumerate(accu):
            if val % k in mod and i - mod[val % k] >= 2:
                return True
            else:
                mod.setdefault(val % k, i)

        return False
