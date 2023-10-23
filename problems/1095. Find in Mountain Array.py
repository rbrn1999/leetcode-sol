# link: https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        memo = {}
        def get_val(index: int) -> int:
            if index not in memo:
                memo[index] = mountain_arr.get(index)
            return memo[index]
            
        n = mountain_arr.length()
        low = 0
        high = n-1
        while low < high:
            mid = low + (high - low) // 2
            if get_val(mid) > get_val(mid+1):
                if get_val(mid) == target:
                    return mid
                high = mid
            else:
                low = mid + 1
        
        peak = low if get_val(low) > get_val(low-1) else low - 1
        print(peak)
        low = 0
        high = peak
        while low <= high:
            mid = low + (high-low) // 2
            if get_val(mid) == target:
                return mid
            elif get_val(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        low = peak + 1
        high = n-1
        while low <= high:
            mid = low + (high-low) // 2
            if get_val(mid) == target:
                return mid
            elif get_val(mid) > target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1