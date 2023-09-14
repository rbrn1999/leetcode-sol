# link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

# Sorting + Intervals: time: O(n + 26·log(26)) space: O(26)
class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        freq_count = {}
        for freq in char_count.values():
            freq_count[freq] = freq_count.get(freq, 0) + 1
        
        freqs = sorted(freq_count.keys())
        slots = [] # list of [start, end]
        deletions = 0
        for i in range(len(freqs)):
            if freqs[i] > 1:
                if i == 0 and freqs[i] > 1:
                    slots.append([1, freqs[i]-1])
                elif freqs[i] > freqs[i-1] + 1:
                    slots.append([freqs[i-1]+1, freqs[i]-1])
            if freq_count[freqs[i]] > 1:
                for _ in range(freq_count[freqs[i]]-1):
                    if not slots:
                        deletions += freqs[i]
                    else:
                        deletions += freqs[i] - slots[-1][1]
                        slots[-1][1] -= 1
                        if slots[-1][1] < slots[-1][0]:
                            slots.pop()
        
        return deletions

# HashMap + Greedy: time: O(n + 26^2), space: O(26)
class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = {}
        used = set()
        deletions = 0
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        
        for _, freq in char_count.items():
            while freq > 0 and freq in used: # at most 25 is used
                deletions += 1
                freq -= 1
            used.add(freq)
        
        return deletions