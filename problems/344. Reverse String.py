# link: https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

# recursive
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        def helper(l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            helper(l, r)

        helper(l, r)
