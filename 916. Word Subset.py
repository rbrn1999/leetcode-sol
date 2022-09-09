# link: https://leetcode.com/problems/word-subsets/
class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def count(word):
            c = [0] * 26
            for letter in word:
                c[ord(letter)-ord('a')] += 1
            return c

        union_b_count = [0]*26
        for b in words2:
            for i, c in enumerate(count(b)):
                union_b_count[i] = max(union_b_count[i], c)

        return [a for a in words1 if all(x >= y for x, y in zip(count(a), union_b_count))]
