# link: https://leetcode.com/problems/second-minimum-time-to-reach-destination/

from collections import defaultdict, deque
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        cur_time = 0
        q.append(1)
        visited = [0] * (n+1)
        visited[1] += 1

        while q:
            next_nodes = set()
            for _ in range(len(q)):
                v = q.popleft()

                for u in graph[v]:
                    if u in next_nodes or visited[u] == 2:
                        continue
                    else:
                        visited[u] += 1
                    if u == n and visited[u] == 2:
                        return cur_time + time
                    next_nodes.add(u)

            q = deque(next_nodes)
            cur_time += time
            if (cur_time // change) % 2 == 1:
                cur_time = (cur_time // change + 1) * change

        return -1
