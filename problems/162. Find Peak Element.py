# link: https://leetcode.com/problems/find-peak-element/
# solution reference: https://leetcode.com/problems/find-peak-element/solutions/127550/find-peak-element/
# solution reference: https://leetcode.com/problems/find-peak-element/solutions/1290642/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left
