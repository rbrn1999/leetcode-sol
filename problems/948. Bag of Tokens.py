# link: https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        score = 0
        max_score = 0
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                max_score = max(max_score, score)
                l += 1
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        
        return max_score
