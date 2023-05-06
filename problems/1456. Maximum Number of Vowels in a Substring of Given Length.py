# link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = len()
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxCount = count
        for i in range(k, len(s)):
            count += int(s[i] in vowels) - int(s[i-k] in vowels)
            maxCount = max(maxCount, count)
        return maxCount

