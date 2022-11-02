# link: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remain = set(range(len(nums)+1))
        for num in nums:
            remain.remove(num)
        return remain.pop()


# one-liner
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(0,len(nums)+1)) - set(nums)).pop()

# math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n+1)) // 2) - sum(nums)

# XOR
# solution reference: https://youtu.be/WnPLSRLSANE
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res
