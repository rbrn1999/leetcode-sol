# link: https://leetcode.com/problems/alien-dictionary/

from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: list[str]) -> str:

        graph = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(len(words)-1):
            l = min(len(words[i]), len(words[i+1]))
            if words[i][:l] == words[i+1][:l] and len(words[i]) > len(words[i+1]):
                return ""
            for j in range(l):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in graph[words[i][j]]:
                        graph[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] += 1
                    break

        q = deque(c for c in indegree if indegree[c] == 0)
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for nextC in graph[c]:
                indegree[nextC] -= 1
                if indegree[nextC] == 0:
                    q.append(nextC)

        return ''.join(result) if len(result) == len(indegree) else ""
