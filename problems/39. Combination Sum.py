# link: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(ind, comb, target):
            if target == 0:
                res.append(comb)
                return
            for i in range(ind, len(candidates)):
                if candidates[i] <= target:
                    helper(i, comb + [candidates[i]], target - candidates[i])

        helper(0, [], target)
        return res

