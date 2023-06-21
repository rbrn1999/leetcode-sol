# link: https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        end = nums[0]
        answer = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                answer.append(str(start) if start == end else f'{start}->{end}')
                start = end = nums[i]
            else:
                end = nums[i]
        answer.append(str(start) if start == end else f'{start}->{end}')
        return answer

