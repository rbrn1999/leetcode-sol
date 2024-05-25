# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        # all nodes are connected, so be chaining, we can apply xor to any pair of nodes
        nums.sort(key = lambda x: (x ^ k) - x, reverse=True)

        for i in range(0, len(nums)-1, 2):
            if nums[i] + nums[i+1] >= (nums[i] ^ k) + (nums[i+1] ^ k):
                break
            else:
                nums[i] ^= k
                nums[i+1] ^= k
        
        if (nums[-1] ^ k) + (nums[-2] ^ k) > nums[-1] + nums[-2]:
            nums[-1] ^= k
            nums[-2] ^= k

        return sum(nums)