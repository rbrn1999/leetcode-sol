# link: https://leetcode.com/problems/daily-temperatures/
# solution reference: https://leetcode.com/problems/daily-temperatures/discuss/1574808/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res
