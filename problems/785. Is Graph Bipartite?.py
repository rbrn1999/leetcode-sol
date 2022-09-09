# link: https://leetcode.com/problems/is-graph-bipartite/
# solution reference: https://www.baeldung.com/cs/graphs-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [None for _ in range(n)]
        
        color[0] = 0        
        q = [0]
        
        while q:
            n1 = q.pop(0)
            for n2 in graph[n1]:
                if color[n2] is None:
                    color[n2] = (color[n1] + 1) % 2
                    q.append(n2)
                elif color[n1] == color[n2]:
                    return False
            if len(q) == 0 and None in color:
                nextGraphRoot = color.index(None)
                q.append(nextGraphRoot)
                color[nextGraphRoot] = 0
                
        
        return True
        