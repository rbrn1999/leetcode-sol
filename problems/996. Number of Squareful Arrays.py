from collections import defaultdict
import math
class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        def isSquare(num: int) -> bool:
            return num == int(math.sqrt(num)) ** 2

        n = len(nums)
        num_count = defaultdict(lambda: 0)
        graph = defaultdict(set)

        for num in nums:
            num_count[num] += 1
        
        unique_nums = list(num_count.keys())
        unique_count = len(unique_nums)
        for i in range(unique_count):
            for j in range(i, unique_count):
                if isSquare(unique_nums[i] + unique_nums[j]):
                    graph[unique_nums[i]].add(unique_nums[j])
                    graph[unique_nums[j]].add(unique_nums[i])

        result = 0
        perm = []
        def dfs(num):
            if len(perm) == n:
                nonlocal result
                result += 1
                return
            for next_num in graph[num]:
                if num_count[next_num] == 0:
                    continue
                num_count[next_num] -= 1
                perm.append(next_num)
                dfs(next_num)
                num_count[next_num] += 1
                perm.pop()

        for num in unique_nums:
            perm = [num]
            num_count[num] -= 1
            dfs(num)
            num_count[num] += 1

        return result