# link: https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        position = [0, 0]
        visited.add((0, 0))
        for direction in path:
            match direction:
                case 'N':
                    position[1] += 1
                case 'S':
                    position[1] -= 1
                case 'E':
                    position[0] += 1
                case 'W':
                    position[0] -= 1
            
            if tuple(position) in visited:
                return True
            else:
                visited.add(tuple(position))
        
        return False