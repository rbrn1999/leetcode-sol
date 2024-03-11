# link: https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {c: 0 for c in order}
        others = []
        for c in s:
            if c in count:
                count[c] += 1
            else:
                others.append(c)
        
        result = []
        for c in order:
            result.append(count[c] * c)
        
        result.extend(others)

        return ''.join(result)