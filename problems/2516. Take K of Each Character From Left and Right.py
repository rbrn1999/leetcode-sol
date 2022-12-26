# link: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_count = Counter(s)
        for char in "abc":
            total_count.setdefault(char, 0)

        if any(count < k for count in total_count.values()):
            return -1

        limit = {c: total_count[c] - k for c in total_count} # max char allowed in the mid sliding window
        n = len(s)

        result = float('inf')
        char_count = defaultdict(lambda: 0)
        l = r = 0

        for r in range(n):
            char_count[s[r]] += 1
            while char_count[s[r]] > limit[s[r]]:
                char_count[s[l]] -= 1
                l += 1
            result = min(result, n - (r-l+1))

        return result

