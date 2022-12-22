# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        answer = [-1, -1]

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target or nums[mid-1] == target:
                right = mid - 1
            else:
                answer[0] = mid
                break
        if nums and answer[0] == -1:
            if nums[left] == target:
                answer[0] = left
            elif left + 1 < len(nums) and nums[left + 1] == target:
                answer[0] = left + 1
            else:
                return answer

        left, right = answer[0], len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target or nums[mid+1] == target:
                left = mid + 1
            else:
                answer[1] = mid
                break

        if nums and answer[1] == -1:
            answer[1] = right if nums[right] == target else right - 1

        return answer
