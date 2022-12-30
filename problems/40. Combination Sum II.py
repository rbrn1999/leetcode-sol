# link: https://leetcode.com/problems/combination-sum-ii/
# solution reference: https://leetcode.com/problems/combination-sum-ii/solutions/16861/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
