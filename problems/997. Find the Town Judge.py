# link: https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = defaultdict(lambda: [True, 0])
        for a, b in trust:
            trustCount[a][0] = False
            trustCount[b][1] += 1

        for i in range(1, n+1):
            if trustCount[i][0] and trustCount[i][1] == n-1:
                return i

        return -1
