# link: https://leetcode.com/problems/encode-and-decode-strings/

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(str(len(s)) + ';' + s for s in strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != ';':
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            strs.append(s[i:i+length])
            i += length

        return strs




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
