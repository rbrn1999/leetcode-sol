# link: https://leetcode.com/problems/queue-reconstruction-by-height/

from sortedcontainers import SortedList

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        # tiebreaker: process the person with the higher k to not mess with the index
        indices = SortedList(range(len(people)))
        result = [[-1, -1] for _ in range(len(people))]

        for h, k in people:
            index = indices[k]
            result[index] = [h, k]
            indices.pop(k)

        return result
