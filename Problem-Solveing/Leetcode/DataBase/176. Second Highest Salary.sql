-- 176. Second Highest Salary| 07-01-2022
SELECT 
MAX(salary)  as SecondHighestSalary 
FROM Employee 
where salary  Not In 
( select max(salary) from Employee )