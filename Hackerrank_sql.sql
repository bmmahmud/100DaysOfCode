/* Revising Aggregations - Averages */ 
select avg(population) from city where district ="California";

/* Average Population - Rount the result with near value no float result */ 
SELECT round(avg(population)) from City ;

/* Japan Population */
SELECT SUM(population) from City where COUNTRYCODE ="JPN";

/* Population Density Difference */
SELECT max(population)-min(population) from City;

/* The Blunder 
here, CEIL = This function returns the smallest integer greater than, or equal to, the specified numeric expression.
calculation = actual - miscalculation
here space is actuall 0 ,that why we replace ) with space cheracter 
*/

SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0',''))) FROM EMPLOYEES;

/* Asian Population: here are two table  */

SELECT SUM(CITY.POPULATION) 
FROM CITY,COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE AND COUNTRY.CONTINENT = 'Asia';











