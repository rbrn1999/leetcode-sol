# link: https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0

        positive_ind = 0
        for i in range(len(satisfaction)):
            if satisfaction[i] > 0:
                positive_ind = i
                break

        cur_sum = sum(satisfaction[positive_ind:])
        cur_coeff = sum([satisfaction[i]*(i-(positive_ind-1)) for i in range(positive_ind, len(satisfaction))])
        max_coeff = cur_coeff
        for i in range(positive_ind-1, -1, -1):
            cur_sum += satisfaction[i]
            cur_coeff += cur_sum
            max_coeff = max(max_coeff, cur_coeff)

        return max_coeff

