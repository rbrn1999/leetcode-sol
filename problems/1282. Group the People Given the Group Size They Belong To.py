# link: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        group = defaultdict(list)
        for i, size in enumerate(groupSizes):
            if len(group[size]) == 0 or len(group[size][-1]) == size:
                group[size].append([])
            group[size][-1].append(i)
        
        answer = []
        for groups in group.values():
            answer.extend(groups)
        return answer