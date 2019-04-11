/* Revising Aggregations - Averages */ 
select avg(population) from city where district ="California";

/* Average Population - Rount the result with near value no float result */ 
SELECT round(avg(population)) from City ;

/* Japan Population */
SELECT SUM(population) from City where COUNTRYCODE ="JPN";

/* Population Density Difference */
SELECT max(population)-min(population) from City;


