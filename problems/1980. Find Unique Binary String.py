# link: 

# Hash Set
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        s = set(int(num, 2) for num in nums)
        cur = 0
        while cur in s:
            cur += 1
        
        return bin(cur)[2:].zfill(n)