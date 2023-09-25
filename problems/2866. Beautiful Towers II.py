# link: https://leetcode.com/problems/beautiful-towers-i/

class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        n = len(maxHeights)
        answer = 1 * n
        for peak in range(n):
            prev = maxHeights[peak]
            height = maxHeights[peak]
            for left in range(peak-1, -1, -1):
                prev = min(prev, maxHeights[left])
                height += prev
            prev = maxHeights[peak]
            for right in maxHeights[peak+1:]:
                prev = min(prev, right)
                height += prev
            answer = max(answer, height)
        
        return answer