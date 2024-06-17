# link: https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        completed = 0 # can form [1...completed]

        for num in nums:
            while num-1 > completed:
                patches += 1
                completed += completed + 1
                if completed >= n:
                    return patches

            completed += num
            if completed >= n:
                return patches

        while n > completed:
            patches += 1
            completed += completed + 1

        return patches
