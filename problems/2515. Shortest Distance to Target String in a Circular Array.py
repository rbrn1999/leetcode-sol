# link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        steps = 0
        for steps in range(n):
            if words[(startIndex+n-steps) % n] == target or words[(startIndex+n+steps) % n] == target:
                return steps

        return -1

