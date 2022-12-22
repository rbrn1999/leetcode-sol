# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(target, left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < target:
                    left = mid + 1
                elif numbers[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        n = len(numbers)
        for i in range(n):
            j = search(target - numbers[i], i+1, n-1)
            if j == -1:
                continue
            return [i+1 ,j+1]

        return [-1, -1]
