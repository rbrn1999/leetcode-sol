# link: https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [names[i] for i in sorted(range(len(names)), key=lambda i: heights[i], reverse=True)]