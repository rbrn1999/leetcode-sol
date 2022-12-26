# link: https://leetcode.com/problems/longest-subsequence-with-limited-sum

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        answer = [0] * m
        nums.sort()
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort()
        pointer = -1
        cur_sum = 0
        for q, i in qs:
            while pointer+1 < n and cur_sum + nums[pointer+1] <= q:
                pointer += 1
                cur_sum += nums[pointer]

            answer[i] = pointer + 1  # (index - 0) + 1

        return answer
