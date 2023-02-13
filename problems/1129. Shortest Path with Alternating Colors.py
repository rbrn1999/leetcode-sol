# link: https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [-1] * n
        graph = defaultdict(lambda: [set(), set()])

        for source, destination in redEdges:
            graph[source][0].add(destination)

        for source, destination in blueEdges:
            graph[source][1].add(destination)

        def bfs(red_path_init: bool):
            distance = 0
            queue = deque([0])
            visited_red = set()
            visited_blue = set()
            useRedPath = red_path_init
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if useRedPath:
                        visited_red.add(node)
                    else:
                        visited_blue.add(node)

                    if answer[node] == -1 or answer[node] > distance:
                        answer[node] = distance

                    neighbors = set()
                    if useRedPath:
                        neighbors = graph[node][0]
                    else:
                        neighbors = graph[node][1]
                    for neighbor in neighbors:
                        if (useRedPath and neighbor in visited_blue) or (not useRedPath and neighbor in visited_red):
                            continue
                        queue.append(neighbor)

                useRedPath = not useRedPath
                distance += 1


        bfs(True)
        bfs(False)
        return answer

