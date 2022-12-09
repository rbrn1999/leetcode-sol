# link: https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.defaultdict(lambda: 0)
        for num in arr:
            counter[num] += 1

        s = set()
        for count in counter.values():
            if count in s:
                return False
            s.add(count)

        return True

