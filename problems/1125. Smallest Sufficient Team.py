# link: https://leetcode.com/problems/smallest-sufficient-team/

from functools import cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        m = len(people)
        d = {skill: i for i, skill in enumerate(req_skills)}

        @cache
        def dfs(i, mask):
            if mask == 2 ** n - 1:
                return [0, []]
            if i == m:
                return [float('inf'), []]

            skip, ans1 = dfs(i+1, mask)
            for skill in people[i]:
                mask |= 2 ** d[skill]
            take, ans2 = dfs(i+1, mask)
            if skip < take+1:
                return [skip, ans1]
            else:
                return [take+1, ans2 + [i]]

        
        return dfs(0, 0)[1]