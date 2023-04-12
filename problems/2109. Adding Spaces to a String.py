# link: https://leetcode.com/problems/adding-spaces-to-a-string/
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        i = 0
        answer_arr = []
        for j in range(len(s)):
            if i != n and spaces[i] == j:
                answer_arr.append(' ')
                i += 1
            answer_arr.append(s[j])
        return ''.join(answer_arr)

