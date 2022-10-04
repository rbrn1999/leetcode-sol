# link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = maxInd = 0
        total = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                maxInd = maxInd if neededTime[maxInd] > neededTime[i] else i
            else:
                if left != i-1:
                    total += sum(neededTime[left:maxInd]) + sum(neededTime[maxInd+1:i])
                    print(total)

                left = maxInd = i

        if left != len(colors)-1:
            total += sum(neededTime[left:maxInd]) + sum(neededTime[maxInd+1:])


        return total
