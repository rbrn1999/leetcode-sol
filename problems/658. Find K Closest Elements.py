# link: https://leetcode.com/problems/find-k-closest-elements/
# solution reference: https://leetcode.com/problems/find-k-closest-elements/solutions/462664/

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # find start of range
        left, right = 0, len(arr) - k

        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid+k] - x: # (x is between[mid, mid+k] and closer to the end) or x is larger than arr[mid+k]
                left = mid + 1
            else: # x smaller than arr[mid] or (x is between arr[mid, mid+k] and closer to the start)
                right = mid
        
        return arr[left: left+k]