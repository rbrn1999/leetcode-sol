# link: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = []
        n = len(s)
        section = numRows*2 - 2
        index = 0
        while index < n:
            result.append(s[index])
            index += section
        for row in range(1, numRows-1):
            section_count = 0
            base = 0
            while base < n:
                if base + row < n:
                    result.append(s[base + row])
                if base + section - row < n:
                    result.append(s[base + section - row])
                base += section

        index = numRows-1
        while index < n:
            result.append(s[index])
            index += section

        return ''.join(result)
