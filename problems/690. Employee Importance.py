# link: https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        id_to_employee = {} # key: id, value: employee

        for employee in employees:
            id_to_employee[employee.id] = employee

        total_value = 0

        def dfs(employeeId: int) -> int:
            employee = id_to_employee[employeeId]
            value = employee.importance
            for subordinateId in employee.subordinates:
                value += dfs(subordinateId)

            return value

        return dfs(id)
