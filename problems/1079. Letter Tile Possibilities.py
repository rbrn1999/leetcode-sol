# link: https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_list = [t for t in tiles]
        def dfs(i: int) -> int:
            if i == len(tile_list):
                return 0
            
            seen = set()
            count = 0
            for j in range(i, len(tile_list)):
                if tile_list[j] in seen:
                    continue
                tile_list[i], tile_list[j] = tile_list[j], tile_list[i]
                seen.add(tile_list[i])
                count += 1 + dfs(i+1)
                tile_list[i], tile_list[j] = tile_list[j], tile_list[i]
            
            return count
        
        return dfs(0)