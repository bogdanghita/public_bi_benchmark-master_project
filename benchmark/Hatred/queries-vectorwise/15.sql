SELECT "Hatred_1"."State " AS "State ",   SUM(1) AS "TEMP(Calculation_251075720248410112)(2109769841)(0)",   CAST(MAX("Hatred_1"."StatePopNum") AS BIGINT) AS "TEMP(Calculation_251075720248410112)(3451088709)(0)",   CAST(MIN("Hatred_1"."StatePopNum") AS BIGINT) AS "TEMP(Calculation_251075720248410112)(3855970114)(0)" FROM "Hatred_1" WHERE (("Hatred_1"."State " <> 'DC') AND ("Hatred_1"."Keyword" IN ('nigger', 'porch monkey'))) GROUP BY 1 HAVING ((SUM(1) >= 30) AND (SUM(1) <= 100000));
