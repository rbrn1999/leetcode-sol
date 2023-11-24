# link: https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = []
        for i in range(len(l)):
            sub_set = set(nums[l[i]:r[i]+1])
            start, end = min(sub_set), max(sub_set)
            if start == end:
                answer.append(True)
                continue
            if (end - start) % (r[i]-l[i]) > 0:
                answer.append(False)
                continue
            diff = (end - start) // (r[i]-l[i])
            valid = True
            for num in range(start, end+1, diff):
                if num not in sub_set:
                    answer.append(False)
                    valid = False
                    break
            if valid:
                answer.append(True)
        
        return answer