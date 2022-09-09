# link: https://leetcode.com/problems/evaluate-division/
# solution reference: https://leetcode.com/problems/evaluate-division/discuss/88275

# For example:
# Given:
# a/b = 2.0, b/c = 3.0
# We can build a directed graph:
# a -- 2.0 --> b -- 3.0 --> c
# If we were asked to find a/c, we have:
# a/c = a/b * b/c = 2.0 * 3.0
# In the graph, it is the product of costs of edges.

# Do notice that, 2 edges need to added into the graph with one given equation,
# because with a/b we also get result of b/a, which is the reciprocal of a/b.

# so the previous example also gives edges:
# c -- 0.333 --> b -- 0.5 --> a

from collections import defaultdict, deque

class Solution():
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)
        
        def build_graph(equations, values):
            def add_edge(f, t, value):
                graph[f].append((t, value))
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            # BFS
            q = deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    # "compress" path for faster look up for the remaining quiries
                    graph[b].append((e, cur_product))
                    graph[e].append((b, 1/cur_product))
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
                        
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]