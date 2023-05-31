# link: https://leetcode.com/problems/jump-game-iv/

from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        valueIndexes = defaultdict(set)
        for i in range(1, n):
            valueIndexes[arr[i]].add(i)
        
        steps = 0
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)

        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()

                if index == n-1:
                    return steps
                if index + 1 not in visited:
                    valueIndexes[arr[index+1]].remove(index+1)
                    visited.add(index + 1)
                    queue.append(index + 1)

                if index - 1 >= 0 and index - 1 not in visited:
                    valueIndexes[arr[index-1]].remove(index-1)
                    visited.add(index - 1)
                    queue.append(index - 1)

                for nextIndex in valueIndexes[arr[index]]:
                    if nextIndex in visited:
                        continue
                    visited.add(nextIndex)
                    queue.append(nextIndex)
                valueIndexes[arr[index]].clear() # It's slower if we use the union difference operation ( set - [nextIndex]), will cause TLE

            steps += 1

        return -1