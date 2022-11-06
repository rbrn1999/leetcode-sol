# link: https://leetcode.com/problems/orderly-queue/
# solution reference: https://leetcode.com/problems/orderly-queue/solution/
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # if k is 1, we can rotate the string
        # if k is greater than 1, we can rotate the substring s[n:] where n is 0~k-1
        # therefore we can eventaully make it in any order we want
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))

