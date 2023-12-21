# link: https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        graph = {}
        for start, end in paths:
            graph[start] = end
        
        city = paths[0][0]
        while city in graph:
            city = graph[city]
        
        return city