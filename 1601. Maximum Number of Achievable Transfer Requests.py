# link: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        status = [0] * n
        result = 0
        def dfs(i, count=0) -> int:
            if i == len(requests):
                if all(i == 0 for i in status):
                    nonlocal result
                    result = max(result, count)
                return
            
            dfs(i+1, count)

            f, t = requests[i]
            status[f] -= 1
            status[t] += 1
            dfs(i+1, count+1)
            status[f] += 1
            status[t] -= 1
        
        dfs(0)
        return result
            