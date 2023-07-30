# link: https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = left + (right-left) // 2
            if arr[mid] <= arr[left]:
                right = mid-1
            elif arr[mid] <= arr[right]:
                left = mid+1
            elif arr[mid] < arr[mid+1]:
                left = mid+1
            elif arr[mid] < arr[mid-1]:
                right = mid-1
            else:
                return mid
        
        return left if arr[left] > arr[right] else right
# slightly slower
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right-left) // 2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        
        return left