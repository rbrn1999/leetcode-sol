# link: https://leetcode.com/problems/strings-differ-by-one-character/description

# Hash One Position at a Time (Rolling Hash)
class Solution:
    def differByOne(self, dict: list[str]) -> bool:
        n = len(dict[0])

        # is the string the same besides the i-th character
        for i in range(n):
            seen_pattern = set()
            for word in dict:
                pattern = word[:i] + '.' + word[i+1:]
                if pattern in seen_pattern:
                    return True
                else:
                    seen_pattern.add(pattern)

        return False

# Hash All Patterns (Memory Limit Exceeded)
class Solution:
    def differByOne(self, dict: list[str]) -> bool:
        pattern_set = set()

        for word in dict:
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                if pattern in pattern_set:
                    return True
                else:
                    pattern_set.add(pattern)

        return False
