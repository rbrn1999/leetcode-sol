# link: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1
        
        for word in words[1:]:
            cur_char_count = {}
            for char in word:
                cur_char_count[char] = cur_char_count.get(char, 0) + 1
            
            for char in list(char_count.keys()):
                if char not in cur_char_count:
                    del char_count[char]
                else:
                    char_count[char] = min(char_count[char], cur_char_count[char])
        
        result = []
        for char, count in char_count.items():
            result.extend([char] * count)
        
        return result
        