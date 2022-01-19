-- 184. Department Highest Salary | 19/01/2022
Select 
dp.name as Department,
emp.name as Employee ,
emp.salary as Salary  
from employee as emp
left join department as dp
on emp.departmentId = dp.id
where (Departmentid,salary) in
(
    select Departmentid,Max(salary) from Employee
    Group By Departmentid
)


-- Select 
-- dp.name as Department,
-- emp.name as Employee ,
-- emp.salary as Salary  
-- from employee as emp
-- left join department as dp
-- on emp.departmentId = dp.id
-- where salary = (Select Max(salary)
-- from Employee)