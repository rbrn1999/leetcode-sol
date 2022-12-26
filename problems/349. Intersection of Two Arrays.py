# link: https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        interSet = set(nums1)
        for num in nums2:
            if num in interSet:
                answer.add(num)

        return list(answer)
