--  link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Write your MySQL query statement below
select e.name as Employee
from Employee as e
join Employee as m
on e.managerId = m.id
and e.salary > m.salary