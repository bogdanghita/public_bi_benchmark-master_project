SELECT CAST("USCensus_2"."REGION" AS BIGINT) AS "REGION",   CAST("USCensus_2"."ST" AS BIGINT) AS "ST (ss13pusa.csv+)",   COUNT(DISTINCT CAST("USCensus_2"."SERIALNO" AS TEXT)) AS "TEMP(Calculation_368169302745513989)(1337797081)(0)",   SUM(CAST("USCensus_2"."Number of Records" AS BIGINT)) AS "TEMP(Calculation_368169302745513989)(3967762572)(0)" FROM "USCensus_2" GROUP BY "USCensus_2"."REGION",   "USCensus_2"."ST",   1,   2;
