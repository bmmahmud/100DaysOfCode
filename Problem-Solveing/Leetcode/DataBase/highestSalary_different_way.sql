-- Hightest salary
Select Max(salary)
from Employee

-- 2nd Highest salary
Select max(salary)
from Employee
where salary < (Select max(salary) from Employee)

-- 2nd Highest salary Not in
Select max(salary)
from Employee
where salary Not IN (Select max(salary) from Employee)

-- 3nd Highest salary Not in
Select max(salary)
from Employee
where salary Not IN (Select max(salary) from Employee where salary < (Select max(salary) from Employee))

-- Nth High correlated nested
Select salary from Employee e1
where N-1 = ( Select count(Distinct salary) from Employee e2
                  where e2.salary>e1.salary)

-- Nth High Limit
 Select Distinct salary 
    from Employee 
      Order By salary DESC
        LIMIT N-1,1

-- 2nd Highest using Limit
Select salary
from Employee
Order By salary DESC
Limit 1,1;