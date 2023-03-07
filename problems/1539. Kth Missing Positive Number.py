# link: https://leetcode.com/problems/kth-missing-positive-number/

# one pass
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr = [0] + arr + [float('inf')]
        prev = 0
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff == 1:
                continue
            if diff - 1 >= k:
                return arr[i-1] + k
            else:
                k -= diff - 1

        return -1

# binary search
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high-low) // 2
            if arr[mid] - (mid+1) < k: # arr[mid] - (mid+1): missing number count in [0, mid]
                low += 1
            else:
                high = mid

        return low + k

