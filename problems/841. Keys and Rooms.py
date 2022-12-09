# link: https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(i):
            visited.add(i)
            for k in rooms[i]:
                if k not in visited:
                    dfs(k)

        dfs(0)

        return len(visited) == len(rooms)
