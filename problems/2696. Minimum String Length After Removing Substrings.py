# link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# Stack
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        char_map = {'B': 'A', 'D': 'C'}
        length = len(s)
        for c in s:
            match c:
                case 'A' | 'C':
                    stack.append(c)
                case c if c in char_map and stack and stack[-1] == char_map[c]:
                    stack.pop()
                    length -= 2
                case _:
                    stack = []

        return length
