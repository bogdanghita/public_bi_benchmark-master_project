--SELECT MAX("MLB_56"."AVG") AS "TEMP(attr:AVG:qk)(3030839854)(0)",   MIN("MLB_56"."AVG") AS "TEMP(attr:AVG:qk)(3417196579)(0)",   MAX("MLB_56"."BABIP") AS "TEMP(attr:BABIP:qk)(4285141330)(0)",   MIN("MLB_56"."BABIP") AS "TEMP(attr:BABIP:qk)(611967120)(0)",   MIN("MLB_56"."FB.") AS "TEMP(attr:FB.:qk)(1278629458)(0)",   MAX("MLB_56"."FB.") AS "TEMP(attr:FB.:qk)(2318961339)(0)",   MIN("MLB_56"."GB.") AS "TEMP(attr:GB.:qk)(1022556664)(0)",   MAX("MLB_56"."GB.") AS "TEMP(attr:GB.:qk)(3109161517)(0)",   MAX("MLB_56"."ISO") AS "TEMP(attr:ISO:qk)(2407168166)(0)",   MIN("MLB_56"."ISO") AS "TEMP(attr:ISO:qk)(3982906464)(0)",   MIN("MLB_56"."LD.") AS "TEMP(attr:LD.:qk)(2248991516)(0)",   MAX("MLB_56"."LD.") AS "TEMP(attr:LD.:qk)(60363815)(0)",   MAX("MLB_56"."OBP") AS "TEMP(attr:OBP:qk)(1266731308)(0)",   MIN("MLB_56"."OBP") AS "TEMP(attr:OBP:qk)(2650212276)(0)",   MIN("MLB_56"."OPS") AS "TEMP(attr:OPS:qk)(1152849410)(0)",   MAX("MLB_56"."OPS") AS "TEMP(attr:OPS:qk)(440288102)(0)",   MAX("MLB_56"."PU.") AS "TEMP(attr:PU.:qk)(142335332)(0)",   MIN("MLB_56"."PU.") AS "TEMP(attr:PU.:qk)(545470000)(0)",   MIN("MLB_56"."SLG") AS "TEMP(attr:SLG:qk)(1844855431)(0)",   MAX("MLB_56"."SLG") AS "TEMP(attr:SLG:qk)(2111292545)(0)",   MAX("MLB_56"."wOBA") AS "TEMP(attr:wOBA:qk)(1583528808)(0)",   MIN("MLB_56"."wOBA") AS "TEMP(attr:wOBA:qk)(2877628247)(0)",   "MLB_56"."league" AS "league",   "MLB_56"."month" AS "month",   CAST("MLB_56"."year" AS BIGINT) AS "year" FROM "MLB_56" WHERE (("MLB_56"."league" = 'PCL') AND ("MLB_56"."month" = 'July') AND (CAST("MLB_56"."year" AS BIGINT) = 2015)) GROUP BY 23,   24,   "MLB_56"."year",   25;
