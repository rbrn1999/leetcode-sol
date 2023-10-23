# link: https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        root_candidates = set(range(n)) - set(leftChild) - set(rightChild)
        if len(root_candidates) != 1:
            return False
        root = next(iter(root_candidates))

        visited = set()
        def dfs(node: int) -> bool:
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])


        return dfs(root) and len(visited) == n