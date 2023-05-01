# link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float('inf')
        maxSalary = float('-inf')
        total = 0
        for num in salary:
            minSalary = min(minSalary, num)
            maxSalary = max(maxSalary, num)
            total += num
        return (total - minSalary - maxSalary) / (len(salary) - 2)

