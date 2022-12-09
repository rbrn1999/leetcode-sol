# link: https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        count_chars = defaultdict(list)
        for char, count in counter.items():
            count_chars[count].append(char)

        counts = sorted(count_chars.keys(), reverse=True)
        result = []
        for count in counts:
            for char in count_chars[count]:
                result.append(char * count)

        return ''.join(result)

