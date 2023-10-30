# link: https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        ans = 0
        for e in range(32):
            count = 0
            for i in range(len(nums)):
                count += nums[i] % 2
                nums[i] //= 2
            if count >= k:
                ans += 2 ** e
        
        return ans