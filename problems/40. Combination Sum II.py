# link: https://leetcode.com/problems/combination-sum-ii/

# Counting
from collections import Counter
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        num_count = Counter(candidates)
        nums = list(num_count.keys())
        result = []

        def dfs(i: int, chosen: list[int], curSum: int) -> None:
            if curSum == target:
                result.append(chosen.copy())
                return
            if curSum > target:
                return
            if i == len(nums):
                return

            for j in range(i, len(nums)):
                for count in range(1, num_count[nums[j]]+1):
                    chosen.append(nums[j])
                    curSum += nums[j]
                    dfs(j+1, chosen, curSum)
                curSum -= nums[j] * num_count[nums[j]]
                del chosen[-num_count[nums[j]]:]

        dfs(0, [], 0)
        return result


# Sorting
# solution reference: https://leetcode.com/problems/combination-sum-ii/solutions/16861/
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()
        result = []
        path = []

        def dfs(cur, target):
            if target == 0:
                result.append(path.copy())
                return
            elif target < 0:
                return

            for i in range(cur, n):
                if i > cur and candidates[i] == candidates[i-1]:
                    continue # we've already run dfs on this number with the same path prefix
                elif candidates[i] > target:
                    return # optimization

                path.append(candidates[i])
                dfs(i+1, target-candidates[i])
                path.pop()

        dfs(0, target)
        return result
