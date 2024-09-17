# link: https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        losting_total = (m + n) * mean - sum(rolls)

        if losting_total < n or losting_total > n * 6:
            return []

        val = losting_total // n
        k = losting_total - n * val

        result = []
        for i in range(n):
            dice = val + (1 if i < k else 0)
            result.append(dice)

        return result
