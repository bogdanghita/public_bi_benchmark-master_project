--SELECT "YaleLanguages_1"."COUNTRY CALC (lkup country NEW) (copy)" AS "COUNTRY CALC (lkup country NEW) (copy)",   SUM(CAST("YaleLanguages_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "YaleLanguages_1" WHERE (("YaleLanguages_1"."BIB_SUPPRESS_IN_OPAC" = 'N') AND ("YaleLanguages_1"."MFHD_SUPPRESS_IN_OPAC" = 'N')) GROUP BY 1;
