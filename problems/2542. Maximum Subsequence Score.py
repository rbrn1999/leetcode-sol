# link: https://leetcode.com/problems/maximum-subsequence-score/

import heapq
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        sorted_indice = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        nums1 = [nums1[i] for i in sorted_indice]
        nums2 = [nums2[i] for i in sorted_indice]
        # ...or use zip(nums1, nums2) then sort by key=lambda x: x[1]

        subSequence = nums1[:k]
        heapq.heapify(subSequence)
        currSum = sum(subSequence)
        answer = nums2[k-1] * currSum
        for i in range(k, len(nums2)):
            num = heapq.heappushpop(subSequence, nums1[i])
            currSum += nums1[i] - num
            answer = max(answer, nums2[i] * currSum)
        
        return answer
