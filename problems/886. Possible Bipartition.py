# link: https://leetcode.com/problems/possible-bipartition/
# solution reference: https://leetcode.com/problems/possible-bipartition/solutions/2834180/possible-bipartition/

from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_dict = defaultdict(set)

        for a, b in dislikes:
            dislikes_dict[a].add(b)
            dislikes_dict[b].add(a)

        groupLabels = [-1] * (n+1) # -1: None, 0: group 0, 1: group 1

        def bfs(node):
            q = deque()
            q.append(node)
            groupLabels[node] = 0

            while q:
                node = q.popleft()
                for dislike in dislikes_dict[node]:
                    if groupLabels[dislike] == -1:
                        groupLabels[dislike] = (groupLabels[node] + 1) % 2
                        q.append(dislike)
                    if groupLabels[dislike] == groupLabels[node]:
                        return False
                    else:
                        pass
            return True

        for i in range(1, n+1):
            if groupLabels[i] == -1 and not bfs(i):
                return False

        return True
