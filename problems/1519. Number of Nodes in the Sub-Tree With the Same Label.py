# link: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        ans = [0] * n
        def dfs(node: int = 0, parent: int = -1) -> list[int]:
            label_count = [0] * 26
            label_count[ord(labels[node]) - ord('a')] += 1
            for child in graph[node]:
                if child == parent:
                    continue
                child_label_count = dfs(child, node)
                for i in range(26):
                    label_count[i] += child_label_count[i]

            ans[node] = label_count[ord(labels[node]) - ord('a')]
            return label_count

        dfs()
        return ans

