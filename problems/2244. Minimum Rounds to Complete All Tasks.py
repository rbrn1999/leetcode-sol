# link: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        days = 0
        for sameTasks in count.values():
            if sameTasks == 1:
                return -1
            days += sameTasks // 3 + (1 if sameTasks % 3 > 0 else 0)

        return days
