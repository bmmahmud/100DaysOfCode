CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
   set n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      Select Distinct salary 
      from Employee Order By salary DESC
      LIMIT n,1
  );
END

#Alternative
-- Select salary from Employee e1
-- where N-1 = ( Select count(Distinct salary from Employee e2
--                   where e2.salary>e1.salary))