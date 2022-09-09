# link: https://leetcode.com/problems/combination-sum-iii/
# reference: https://leetcode.com/problems/combination-sum-iii/discuss/842764/Python-backtrack-solution-explained
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        answer = []
        def helper(k, n, comb):
            if k<0 or n<0:
                return
            if k == 0 and n == 0:
                nonlocal answer
                answer.append(comb)
                return
            start = comb[-1] + 1 if len(comb)>0 else 1
            for i in range(start, 10):
                helper(k-1, n-i, comb + [i])

        
        helper(k, n, [])
        return answer