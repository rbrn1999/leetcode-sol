# link: https://leetcode.com/problems/naming-a-company/
# solution reference: https://leetcode.com/problems/naming-a-company/solutions/2141038/python-explanation-with-pictures-group/

import string
from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        starting_suffix = defaultdict(set)
        for idea in ideas:
            starting_suffix[idea[0]].add(idea[1:])

        start_chars = list(starting_suffix.keys())
        n = len(start_chars)

        count = 0
        for start_ind_1 in range(n-1):
            for start_ind_2 in range(start_ind_1 + 1, n):
                start_1, start_2 = start_chars[start_ind_1], start_chars[start_ind_2]
                intersect = len(starting_suffix[start_1] & starting_suffix[start_2])
                unique1 = len(starting_suffix[start_1]) - intersect
                unique2 = len(starting_suffix[start_2]) - intersect
                count += 2 * unique1 * unique2

        return count
