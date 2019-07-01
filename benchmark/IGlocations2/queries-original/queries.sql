SELECT "IGlocations2_1"."Calculation_1750724145742463" AS "Calculation_1750724145742463",   "IGlocations2_1"."Calculation_9330724145728972" AS "Calculation_9330724145728972" FROM "IGlocations2_1" WHERE ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) GROUP BY 1,   2
SELECT "IGlocations2_1"."Calculation_1750724145742463" AS "Calculation_1750724145742463",   "IGlocations2_1"."Calculation_9330724145728972" AS "Calculation_9330724145728972",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE (("IGlocations2_1"."Calculation_1750724145742463" = '-157.83000000000001'::double) AND ("IGlocations2_1"."Calculation_9330724145728972" = '21.280000000000001'::double) AND ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas'))) GROUP BY 1,   2
SELECT "IGlocations2_1"."Calculation_8090724143600502" AS "Calculation_8090724143600502",   "IGlocations2_1"."city" AS "city",   "IGlocations2_1"."state" AS "state",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE (("IGlocations2_1"."Calculation_8090724143600502" = 'Drunk') AND ("IGlocations2_1"."city" <> 'Unalaska') AND ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) AND ("IGlocations2_1"."Calculation_4370724142342227" = 'Beach')) GROUP BY 1,   2,   3
SELECT "IGlocations2_1"."State (copy)" AS "State (copy)" FROM "IGlocations2_1" GROUP BY 1 ORDER BY "State (copy)" ASC 
SELECT "IGlocations2_1"."city" AS "city",   "IGlocations2_1"."media_type" AS "media_type",   "IGlocations2_1"."state" AS "state",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) GROUP BY 1,   2,   3 HAVING ((SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) >= 500) AND (SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) <= 99103))
SELECT "IGlocations2_1"."city" AS "city",   "IGlocations2_1"."state" AS "state",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE (("IGlocations2_1"."city" <> 'Unalaska') AND ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) AND ("IGlocations2_1"."Calculation_4370724142342227" = 'Beach')) GROUP BY 1,   2
SELECT "IGlocations2_1"."latitude" AS "latitude",   "IGlocations2_1"."longitude" AS "longitude",   CAST(EXTRACT(MONTH FROM "IGlocations2_1"."created_time") AS BIGINT) AS "mn:created_time:ok",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE (("IGlocations2_1"."Calculation_1750724145742463" = '-157.83000000000001'::double) AND ("IGlocations2_1"."Calculation_9330724145728972" = '21.280000000000001'::double) AND ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas'))) GROUP BY 1,   2,   3
SELECT "IGlocations2_1"."media_type" AS "media_type",   "IGlocations2_1"."state" AS "state",   SUM(CAST("IGlocations2_1"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_1" WHERE ("IGlocations2_1"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) GROUP BY 1,   2
SELECT "IGlocations2_2"."Calculation_1750724145742463" AS "Calculation_1750724145742463",   "IGlocations2_2"."Calculation_9330724145728972" AS "Calculation_9330724145728972",   "IGlocations2_2"."city" AS "city",   "IGlocations2_2"."country" AS "country",   "IGlocations2_2"."state" AS "state",   SUM(CAST("IGlocations2_2"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_2" WHERE (("IGlocations2_2"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) AND ("IGlocations2_2"."State (copy)" = 'Alaska')) GROUP BY 1,   2,   3,   4,   5
SELECT "IGlocations2_2"."Calculation_1750724145742463" AS "Calculation_1750724145742463",   "IGlocations2_2"."Calculation_9330724145728972" AS "Calculation_9330724145728972",   "IGlocations2_2"."state" AS "state",   SUM(CAST("IGlocations2_2"."like_count" AS BIGINT)) AS "sum:like_count:ok" FROM "IGlocations2_2" WHERE (("IGlocations2_2"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) AND ("IGlocations2_2"."State (copy)" = 'Alaska')) GROUP BY 1,   2,   3
SELECT "IGlocations2_2"."Calculation_8090724143600502" AS "Calculation_8090724143600502",   "IGlocations2_2"."city" AS "city",   "IGlocations2_2"."state" AS "state",   SUM(CAST("IGlocations2_2"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_2" WHERE (("IGlocations2_2"."Calculation_8090724143600502" = 'Bar') AND ("IGlocations2_2"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas')) AND ("IGlocations2_2"."State (copy)" = 'Alaska')) GROUP BY 1,   2,   3
SELECT "IGlocations2_2"."State (copy)" AS "State (copy)" FROM "IGlocations2_2" GROUP BY 1 ORDER BY "State (copy)" ASC 
SELECT "IGlocations2_2"."city" AS "city",   SUM(CAST("IGlocations2_2"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok" FROM "IGlocations2_2" WHERE (("IGlocations2_2"."State (copy)" = 'Alaska') AND ("IGlocations2_2"."state" IN ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas'))) GROUP BY 1
