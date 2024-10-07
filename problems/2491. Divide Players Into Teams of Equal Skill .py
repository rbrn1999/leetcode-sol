# link: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from collections import Counter
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        target = sum(skill) // ((len(skill)) // 2)
        count = Counter(skill)
        result = 0
        for s, c in count.items():
            if target-s == s:
                if c % 2 == 1:
                    return -1
                else:
                    result += c//2 * s * s

                continue

            other_count = count.get(target-s, 0)
            if other_count != -1 and c != other_count:
                return -1
            if other_count != -1:
                result += c * s * (target-s)
                count[s] = -1

        return result
