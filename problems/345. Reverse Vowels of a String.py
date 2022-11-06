# link: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        res = [c for c in s]
        l = 0
        r = len(s)-1
        while l < r:
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1
            elif s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(res)# link: https://leetcode.com/problems/reverse-vowels-of-a-string/

    class Solution:
            def reverseVowels(self, s: str) -> str:
                        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
                                res = [c for c in s]
                                        l = 0
                                                r = len(s)-1
                                                        while l < r:
                                                                        if res[l] in vowels and res[r] in vowels:
                                                                                            res[l], res[r] = res[r], res[l]
                                                                                                            l += 1
                                                                                                                            r -= 1
                                                                                                                                        elif s[l] in vowels:
                                                                                                                                                            r -= 1
                                                                                                                                                                        elif s[r] in vowels:
                                                                                                                                                                                            l += 1
                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            l += 1
                                                                                                                                                                                                                                            r -= 1
                                                                                                                                                                                                                                                    return ''.join(res)
