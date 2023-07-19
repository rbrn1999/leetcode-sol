# link: https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        children = [0] * n

        def dfs(i, zero_count):
            if n - i < zero_count:
                return float('inf')
            
            if i == n:
                return max(children)
            
            answer = float('inf')
            for j in range(k):
                zero_count -= int(children[j] == 0)
                children[j] += cookies[i]
                answer = min(answer, dfs(i+1, zero_count))
                children[j] -= cookies[i]
                zero_count += int(children[j] == 0)
            
            return answer
        
        return dfs(0, k)
    