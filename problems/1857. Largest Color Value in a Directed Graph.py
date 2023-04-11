# link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from functools import cache
from collections import defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)

        visited = set()
        @cache
        def dfs(node: int) -> dict:
            color_values = defaultdict(int)
            if node in visited:
                return {'_': -1}
            else:
                visited.add(node)

            for child in graph[node]:
                for character, child_value in dfs(child).items():
                    if child_value == -1:
                        return {'_': -1}
                    color_values[character] = max(color_values[character], child_value)
            color_values[colors[node]] += 1
            return color_values

        answer = 0
        for i in range(len(colors)):
            visited = set()
            values = dfs(i).values()
            if -1 in values:
                return -1
            answer = max(answer, max(values))

        return answer

