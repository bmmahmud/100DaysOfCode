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

/* Weather Observation Station 2 */
select ROUND(sum(LAT_N),2) as lat,
ROUND (sum(LONG_W),2) as lon from STATION; 

/* Weather Observation Station 13| 
BETWEEN return only 1 or 0...that's why we can't use it here */

Select ROUND(sum(LAT_N),4)
from STATION where LAT_N >38.7800 AND LAT_N <137.2345;

/* Weather Observation Station 14 */
Select ROUND(max(LAT_N),4)
from STATION where LAT_N <137.2345;
/* Weather Observation Station 15 */
SELECT ROUND(LONG_W,4) FROM STATION WHERE 
LAT_N = (SELECT MAX(LAT_N)
FROM STATION WHERE LAT_N <137.2345;)
/* Weather Observation Station 16 */
Select ROUND(min(LAT_N),4)
from STATION where LAT_N >38.7800;


/* Average Population of Each Continent */
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;




