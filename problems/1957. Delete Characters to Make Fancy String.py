# link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        streak = 1
        char_list = [s[0]]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                if streak < 2:
                    streak += 1
                else:
                    continue
            else:
                streak = 1
            char_list.append(s[i])

        return ''.join(char_list)
