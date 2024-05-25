#link: https://leetcode.com/problems/stickers-to-spell-word/description/

from collections import Counter
class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        target_freq = Counter(target)
        char_set = set(target_freq.keys())
        sticker_freqs = []
        for sticker in stickers:
            freq = Counter(sticker)
            for c in list(freq.keys()):
                if c in char_set:
                    char_set.remove(c)
                if c not in target_freq:
                    del freq[c]

            sticker_freqs.append(freq)

        if len(char_set) > 0:
            return -1
        
        keep = [True] * len(sticker_freqs)
        for i in range(len(sticker_freqs)):
            for j in range(len(sticker_freqs)):
                if i == j:
                    continue

                if i < j and sticker_freqs[i] == sticker_freqs[j]:
                    keep[i] = True
                    break

                keepSticker = False
                for c in sticker_freqs[i]:
                    if c not in sticker_freqs[j] or sticker_freqs[i][c] > sticker_freqs[j][c]:
                        keepSticker = True
                        break
                
                keep[i] = keepSticker
                    
                if not keep[i]:
                    break
                
        
        sticker_freqs = [sticker_freqs[i] for i in range(len(sticker_freqs)) if keep[i]]
        memo = {}
        def dfs(i: int, t_freq: dict) -> int:
            freq_array = [0] * 26
            for c, freq in t_freq.items():
                freq_array[ord(c) - ord('a')] = freq
            key = (i, tuple(freq_array))
            if key in memo:
                return memo[key]
            if i == len(sticker_freqs):
                if all(val <= 0 for val in t_freq.values()):
                    return 0
                else:
                    return float('inf')
            
            count = dfs(i+1, t_freq.copy())
            sticker_count = 0
            while True:
                if all(t_freq[c] == 0 for c in sticker_freqs[i]):
                    break

                sticker_count += 1
                for c, freq in sticker_freqs[i].items():
                    t_freq[c] = max(0, t_freq[c] - freq)

                count = min(count, sticker_count + dfs(i, t_freq.copy()))

            memo[key] = count
            return count
        
        return dfs(0, target_freq)