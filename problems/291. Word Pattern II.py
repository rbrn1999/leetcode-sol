# link: https://leetcode.com/problems/word-pattern-ii/


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(i: int, j: int, mapping: dict, used: set) -> bool:
            if i == len(pattern):
                return j == len(s)
            
            if pattern[i] in mapping:
                if mapping[pattern[i]] != s[j:j+len(mapping[pattern[i]])]:
                    return False
                else:
                    return dfs(i+1, j+len(mapping[pattern[i]]), mapping, used)
            
            # try every mapping
            l = j
            for r in range(l+1, len(s)+1): # word: [l, r)
                if s[l:r] in used:
                    continue
                
                mapping[pattern[i]] = s[l:r]
                used.add(s[l:r])
                if dfs(i+1, r, mapping, used):
                    return True
                used.remove(s[l:r])

            if pattern[i] in mapping:
                del mapping[pattern[i]]

            return False
        
        return dfs(0, 0, {}, set())
        
