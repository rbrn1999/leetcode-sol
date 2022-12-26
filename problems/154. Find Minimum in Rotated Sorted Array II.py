# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        def search(left, right):
            if left >= right:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] < nums[right] or (nums[mid] == nums[right] and nums[mid] != nums[left]):
                return search(left, mid)
            elif nums[mid] > nums[right]:
                return search(mid+1, right)
            else:
                return min(search(left, mid-1), search(mid+1, right))


        return search(left, right)
