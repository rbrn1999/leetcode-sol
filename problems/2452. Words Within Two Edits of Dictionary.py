# link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res = []
        n = len(queries[0])
        for q in queries:
            for word in dictionary:
                valid = True
                diff = 0
                for i in range(n):
                    diff += int(q[i] != word[i])
                    if diff > 2:
                        valid = False
                        break
                if valid:
                    res.append(q)
                    break
        return res
            