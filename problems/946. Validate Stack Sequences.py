# link: https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        seen = set()
        stack = []
        i = 0
        for pop in popped:
            while pop not in seen and i < len(pushed):
                stack.append(pushed[i])
                seen.add(pushed[i])
                i += 1

            if not stack or stack[-1] != pop:
                return False
            else:
                stack.pop()

        return True

