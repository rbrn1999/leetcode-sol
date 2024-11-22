# link: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr)-1
        while l+1 < len(arr) and arr[l] <= arr[l+1]:
            l += 1
        if l == len(arr)-1:
            return 0
        while r-1 >= 0 and arr[r-1] <= arr[r]:
            r -= 1


        result = r
        j = r
        while j < len(arr) and arr[l] > arr[j]:
            j += 1

        for i in range(l, -1, -1):
            while j > r and arr[j-1] >= arr[i]:
                j -= 1
            result = min(result, j-i-1)

        return result
