# link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# solution reference: https://youtu.be/U8XENwh8Oy8

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bsearch(low, high):
            if low > high:
                return -1
            
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]: # mid at left portion
                if target > nums[mid] or target < nums[low]: # (larger than mid) or (less than mid and smaller than low)
                    return bsearch(mid+1, high)
                else: #(less than mid and larger than low)
                    return bsearch(low, mid-1)
            else:                      # mid at right portion
                if target < nums[mid] or target > nums[high]: # (less than mid) or (larger than mid and larger than high)
                    return bsearch(low, mid-1)
                else: # (larger than mid and lower than high)
                    return bsearch(mid+1, high)

        return bsearch(0, len(nums)-1)