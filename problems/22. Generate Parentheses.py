# link: https://leetcode.com/problems/generate-parentheses/
# solution reference: https://leetcode.com/problems/generate-parentheses/solutions/10100/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def dfs(s="", open_count=0, close_count=0):
            if open_count + close_count == 2*n:
                if open_count == close_count:
                    result.append(s)
                return
            
            if open_count < n:
                dfs(s+'(', open_count+1, close_count)
            if close_count < open_count:
                dfs(s+')', open_count, close_count+1)
        
        dfs()
        return result