--SELECT COUNT(DISTINCT "CommonGovernment_13"."a_aid_acontid_piid") AS "ctd:a_aid_acontid_piid:ok",   SUM(CAST("CommonGovernment_13"."Number of Records" AS BIGINT)) AS "sum:Number of Records:ok",   SUM("CommonGovernment_13"."obligatedamount") AS "sum:obligatedamount:ok",   TABLEAU.TO_DATETIME(DATE_TRUNC('MONTH', TABLEAU.NORMALIZE_DATETIME(cast("CommonGovernment_13"."signeddate" as DATE))), cast("CommonGovernment_13"."signeddate" as DATE)) AS "tmn:signeddate:ok" FROM "CommonGovernment_13" WHERE (("CommonGovernment_13"."refidvid_piid" IN ('', ' ')) OR ("CommonGovernment_13"."refidvid_piid" IS NULL)) GROUP BY 4;