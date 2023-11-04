# link: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        return max(max(left if left else [0]), n - min(right if right else [n]))