--SELECT TABLEAU.TO_DATETIME(DATE_TRUNC('DAY', TABLEAU.NORMALIZE_DATETIME("HashTags_1"."Calculation_6520205001837946")), "HashTags_1"."Calculation_6520205001837946") AS "tdy:Calculation_6520205001837946:ok" FROM "HashTags_1" GROUP BY 1 ORDER BY "tdy:Calculation_6520205001837946:ok" ASC ;
