SELECT MAX("MLB_14"."AVG") AS "TEMP(attr:AVG:qk)(3030839854)(0)",   MIN("MLB_14"."AVG") AS "TEMP(attr:AVG:qk)(3417196579)(0)",   MAX("MLB_14"."BABIP") AS "TEMP(attr:BABIP:qk)(4285141330)(0)",   MIN("MLB_14"."BABIP") AS "TEMP(attr:BABIP:qk)(611967120)(0)",   MAX("MLB_14"."ISO") AS "TEMP(attr:ISO:qk)(2407168166)(0)",   MIN("MLB_14"."ISO") AS "TEMP(attr:ISO:qk)(3982906464)(0)",   MAX("MLB_14"."wOBA") AS "TEMP(attr:wOBA:qk)(1583528808)(0)",   MIN("MLB_14"."wOBA") AS "TEMP(attr:wOBA:qk)(2877628247)(0)",   "MLB_14"."field" AS "field",   "MLB_14"."league" AS "league",   "MLB_14"."stand" AS "stand",   CAST("MLB_14"."year" AS BIGINT) AS "year" FROM "MLB_14" WHERE (("MLB_14"."field" = 'Center') AND ("MLB_14"."league" = 'PCL') AND ("MLB_14"."stand" = 'R') AND (CAST("MLB_14"."year" AS BIGINT) = 2015)) GROUP BY "field", "league", "stand", "MLB_14"."year", "year";