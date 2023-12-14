# link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        prev = -1
        count = 0
        for num in arr:
            if num == prev:
                count += 1
            else:
                count = 1
                prev = num
            if count > n//4:
                return num
        
        return -1