# link: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        edges = defaultdict(list)
        head_and_tail = set()
        for a, b in adjacentPairs:
            if a in head_and_tail:
                head_and_tail.remove(a)
            else:
                head_and_tail.add(a)
            if b in head_and_tail:
                head_and_tail.remove(b)
            else:
                head_and_tail.add(b)

            edges[a].append(b)
            edges[b].append(a)
        
        ans = [next(iter(head_and_tail))]
        while True:
            next_element = None
            for e in edges[ans[-1]]:
                if len(ans) > 1 and ans[-2] == e:
                    continue
                next_element = e

            if next_element is not None:
                ans.append(next_element)
            else:
                break

        return ans