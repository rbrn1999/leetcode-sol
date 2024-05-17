# link: https://leetcode.com/problems/redundant-connection-ii/

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(root: int, removed_edge: list[int], visited: set):
            if root in visited:
                return False

            visited.add(root)
            for child in graph[root]:
                if [root, child] == removed_edge:
                    continue
                if not dfs(child, removed_edge, visited):
                    return False
            
            return True
        
        def findCycle(root: int, visited: set, cycle_nodes: set) -> bool:
            if root in visited:
                while stack and stack[-1] != root:
                    cycle_nodes.add(stack.pop())
                cycle_nodes.add(root)
                return True
            else:
                stack.append(root)
                visited.add(root)
            
            for child in graph[root]:
                if findCycle(child, visited, cycle_nodes):
                    return True

            if stack:
                stack.pop()
            return False


        graph = defaultdict(list)
        n = len(edges)
        indegree = [[] for _ in range(n)]

        for par, child in edges:
            graph[par].append(child)
            indegree[child-1].append(par)
        
        double_indegree_node = -1
        root = -1
        for i in range(n):
            if len(indegree[i]) == 2:
                double_indegree_node = i + 1
            if len(indegree[i]) == 0:
                root = i + 1
        
        # if there's a node with indegree = 2, one of the edge must be the redundant edge
        # try removing the edge and see if the tree is valid
        if double_indegree_node != -1:
            visited = set()
            edge = [indegree[double_indegree_node-1][1], double_indegree_node]
            if dfs(root, edge, visited) and len(visited) == n:
                return edge
            else:
                return [indegree[double_indegree_node-1][0], double_indegree_node]

        
        # find nodes in the cycle and find the last appeared edge in the cycle

        stack = []
        prev_visited = set() # for not traversing the same nodes over and over agian
        visited = set() # for detecting cycle
        cycle_nodes = set()


        for root in range(1, n+1):
            if root in prev_visited:
                continue
            prev_visited.update(visited)
            visited = set()
            if findCycle(root, visited, cycle_nodes):
                break
        
        
        for par, child in reversed(edges):
            if par in cycle_nodes and child in cycle_nodes:
                return [par, child]
        
        return [-1, -1]