# link: https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(chr(ord(chars[-1])+1))
        l = 0
        ptr = 0
        for r in range(len(chars)):
            if chars[r] != chars[l]:
                chars[ptr] = chars[l]
                ptr += 1
                if r - l > 1:
                    count = str(r - l)
                    chars[ptr:ptr+len(count)] = [digit for digit in count]
                    ptr += len(count)

                l = r

        return ptr

