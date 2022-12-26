# link: https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        state = 0
        i = 0
        result = 0
        for j in range(n):
            if forts[j] == 1:
                if state == -1:
                    result = max(result, j - i - 1)
                i = j
                state = 1
            elif forts[j] == -1:
                if state == 1:
                    result = max(result, j - i - 1)
                i = j
                state = -1

        return result
