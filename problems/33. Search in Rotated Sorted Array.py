# link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# solution reference: https://youtu.be/U8XENwh8Oy8

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # left portion of the array
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # right portion of the array
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1