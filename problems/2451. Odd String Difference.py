# link: https://leetcode.com/problems/odd-string-difference/

class Solution:
    def oddString(self, words: list[str]) -> str:
        diffs = {}
        for word in words:
            diff = tuple([ord(word[i])-ord(word[i-1]) for i in range(1, len(word))])
            if diff in diffs:
                diffs[diff].append(word)
                if len(diffs) > 1:
                    del diffs[diff]
                    for words in diffs.values():
                        return words[0]
            elif len(diffs) == 1 and len(list(diffs.values())[0]) > 1:
                return word
            else:
                diffs[diff] = [word]