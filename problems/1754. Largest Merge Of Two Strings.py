# link: https://leetcode.com/problems/largest-merge-of-two-strings/submissions/
class Solution:
    def largestMerge(self, a, b):
        i = j = 0
        ans = ""
        while i < len(a) and j < len(b):
            if a[i:] > b[j:]:
                ans += a[i]
                i += 1
            else:
                ans += b[j]
                j += 1
                
        # append the remaining
        ans += a[i:] + b[j:]
        return ans

        # "abc" > "ab"
        # We can get to 'c' faster when we choose "abc"

        # "aba" > "aaz"
        # The first position 'b' can be is at index 1, for 'z' it's index 2
        # The lower index matters more, therefore chooing "aba" is better