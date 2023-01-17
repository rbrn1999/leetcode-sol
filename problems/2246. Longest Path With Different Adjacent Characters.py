# link: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

import collections
class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        graph = collections.defaultdict(set)
        for node in range(len(parent)):
            graph[parent[node]].add(node)

        def dfs(node: int) -> list[int]: # return: (cur_path, max_path)
            longest_paths = [0, 0]
            max_path = 0
            for child in graph[node]:
                child_path, child_max = dfs(child)
                max_path = max(max_path, child_max)
                if s[child] == s[node]:
                    continue
                if child_path >= longest_paths[0]:
                    longest_paths = [child_path, longest_paths[0]]
                elif child_path > longest_paths[1]:
                    longest_paths[1] = child_path

            max_path = max(max_path, sum(longest_paths) + 1)
            return longest_paths[0] + 1, max_path

        return dfs(0)[1]

