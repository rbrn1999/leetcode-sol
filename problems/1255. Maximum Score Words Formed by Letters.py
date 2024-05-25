# link: https://leetcode.com/problems/maximum-score-words-formed-by-letters/

from collections import Counter
class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        word_char_counts = []
        word_scores = []
        letter_count = Counter(letters)

        for word in words:
            word_char_counts.append(Counter(word))
        
        for word in words:
            word_scores.append(0)
            for c in word:
                word_scores[-1] += score[ord(c) - ord('a')]

        def dfs(i: int, letter_count: dict) -> int:
            if i == len(words):
                return 0
            
            current_score = dfs(i+1, letter_count)

            canUse = True
            for c, count in word_char_counts[i].items():
                if count > letter_count[c]:
                    canUse = False

                letter_count[c] -= count
            
            if canUse:
                current_score = max(current_score, word_scores[i] + dfs(i+1, letter_count))

            # restore the state of the letter_count dictionary
            for c, count in word_char_counts[i].items():
                if count > letter_count[c]:
                    canUse = False

                letter_count[c] += count 
            
            return current_score
        
        return dfs(0, letter_count)
