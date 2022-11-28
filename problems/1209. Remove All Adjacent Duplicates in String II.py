# link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #[char, count]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    del stack[-1]
            else:
                stack.append([c, 1])

        result = ""
        for char, count in stack:
            result += char*count
        return result
