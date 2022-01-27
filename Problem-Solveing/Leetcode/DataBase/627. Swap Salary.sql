--  627. Swap Salary | 07-01-2022

UPDATE salary
SET sex = CASE WHEN sex = 'm' THEN 'f' 
               WHEN sex = 'f' THEN 'm' END
WHERE sex IN ('f','m')