# link: https://leetcode.com/problems/advantage-shuffle/
from collections import deque
from curses.ascii import SO
class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = deque(sorted(nums1, reverse=True))
        nums2 = sorted([(i, v) for i, v in enumerate(nums2)], key=lambda x: x[1], reverse=True)
        result = [-1] * len(nums1)

        for i, v in nums2: # compare to the largest to the smallest nums2
            if nums1[0] > v:
                result[i] = nums1.popleft()
            else: # assign the smallest nums1 if can't beat the current nums2
                result[i] = nums1.pop()
        
        return result

nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
print(Solution().advantageCount(nums1, nums2))