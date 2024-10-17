# link: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0 # total swaps
        swapped = 0 # swapped ']'s that are not used
        opening = 0 # unclosed '['s
        for c in s:
            if c == '[':
                opening += 1
            elif opening > 0:
                opening -= 1
            elif swapped > 0:
                swapped -= 1
            else:
                swaps += 1
                swapped += 1

        return swaps
