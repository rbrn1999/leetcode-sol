# link: https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def gainHelper(self, s: str, x: int, y: int) -> int:
        score = 0
        first_letter_count = 0
        second_letter_count = 0
        high_points = x
        low_points = y
        first_letter = 'a'
        second_letter = 'b'
        if x < y:
            high_points = y
            low_points = x
            first_letter = 'b'
            second_letter = 'a'


        for c in s:
            if c == first_letter:
                first_letter_count += 1
            elif first_letter_count > 0:
                first_letter_count -= 1
                score += high_points
            else:
                second_letter_count += 1

        score += min(first_letter_count, second_letter_count) * low_points

        return score


    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        l = 0
        for r in range(len(s)):
            if s[r] != 'a' and s[r] != 'b':
                if l != r:
                    score += self.gainHelper(s[l:r], x, y)
                l = r + 1

        if l < len(s)-1:
            score += self.gainHelper(s[l:], x, y)

        return score
