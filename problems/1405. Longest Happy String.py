# link: https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        char_count = {'a': a, 'b': b, 'c': c, '_': 0}
        while any(count > 0 for count in char_count.values()):
            first = '_'
            second = '_'
            for c, count in char_count.items():
                if count > char_count[first]:
                    second = first
                    first = c
                elif count > char_count[second]:
                    second = c     

            if len(chars) < 2 or ''.join(chars[-2:]) != first * 2:
                chars.append(first)
                char_count[first] -= 1
            else:
                if char_count[second] == 0:
                    break
                else:
                    chars.append(second)
                    char_count[second] -= 1
            
        return ''.join(chars)