# link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evenSum = sum(num for num in nums if num%2 == 0)
        for val, index in queries:
            wasEven = nums[index] % 2 == 0
            nums[index] += val
            if nums[index]%2 == 1 and wasEven:
                evenSum -= (nums[index]-val)
            elif nums[index]%2 == 0 and wasEven:
                evenSum += val
            elif nums[index]%2 == 0 and not wasEven:
                evenSum += nums[index]
            else:
                pass
            ans.append(evenSum)
        return ans