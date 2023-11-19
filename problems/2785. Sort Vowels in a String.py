# link: https://leetcode.com/problems/sort-vowels-in-a-string/

# Sort
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        positions = []
        for i, c in enumerate(s):
            if c.lower() in vowels_set:
                vowels.append(c)
                positions.append(i)
        
        t = list(s)
        vowels.sort()
        for i in range(len(positions)):
            t[positions[i]] = vowels[i]
        
        return ''.join(t)
    
# Counting Sort
from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        count = defaultdict(int)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c.lower() in vowels_set:
                count[c] += 1
        
        vowels_freq = [[c, freq] for c, freq in count.items()]
        vowels_freq.sort(key=lambda x: x[0], reverse=True)

        t = []
        for i in range(len(s)):
            if s[i].lower() not in vowels_set:
                t.append(s[i])
            else:
                t.append(vowels_freq[-1][0])
                vowels_freq[-1][1] -= 1
                if vowels_freq[-1][1] == 0:
                    vowels_freq.pop()
        
        return ''.join(t)