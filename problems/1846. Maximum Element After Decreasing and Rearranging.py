# link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

# Sorting
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1

        return arr[-1]

# Count Frequency
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        freq = [0] * (n+1)
        for num in arr:
            freq[min(num, n)] += 1
        
        cur = 0
        for num in range(1, n+1):
            cur = min(cur + freq[num], num) # decrease the extra "num"s to fill the blank between cur and num
        
        return cur
