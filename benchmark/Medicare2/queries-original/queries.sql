SELECT "Medicare2_1"."provider_type" AS "provider_type" FROM "Medicare2_1" WHERE ("Medicare2_1"."nppes_provider_state" = 'NY') GROUP BY 1 ORDER BY "provider_type" ASC 
SELECT "Medicare2_2"."hcpcs_description" AS "hcpcs_description" FROM "Medicare2_2" WHERE ("Medicare2_2"."nppes_provider_state" = 'NY') GROUP BY 1 ORDER BY "hcpcs_description" ASC 
SELECT "Medicare2_2"."hcpcs_description" AS "hcpcs_description",   "Medicare2_2"."nppes_entity_code" AS "nppes_entity_code",   "Medicare2_2"."provider_type" AS "provider_type" FROM "Medicare2_2" WHERE (("Medicare2_2"."nppes_provider_state" = 'NY') AND ("Medicare2_2"."nppes_provider_country" = 'US')) GROUP BY 1,   2,   3
SELECT "Medicare2_2"."hcpcs_description" AS "hcpcs_description",   "Medicare2_2"."provider_type" AS "provider_type" FROM "Medicare2_2" WHERE (("Medicare2_2"."nppes_provider_state" = 'NY') AND ("Medicare2_2"."nppes_provider_country" = 'US')) GROUP BY 1,   2
SELECT "Medicare2_2"."nppes_entity_code" AS "nppes_entity_code" FROM "Medicare2_2" WHERE ("Medicare2_2"."nppes_provider_state" = 'NY') GROUP BY 1 ORDER BY "nppes_entity_code" ASC 
SELECT "Medicare2_2"."provider_type" AS "provider_type" FROM "Medicare2_2" WHERE ("Medicare2_2"."nppes_provider_state" = 'NY') GROUP BY 1 ORDER BY "provider_type" ASC 
SELECT CAST("Medicare2_2"."bene_unique_cnt" AS BIGINT) AS "bene_unique_cnt (copy)",   CAST("Medicare2_2"."hcpcs_code" AS BIGINT) AS "hcpcs_code",   "Medicare2_2"."hcpcs_description" AS "hcpcs_description",   CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT) AS "line_srvc_cnt (copy)",   "Medicare2_2"."nppes_provider_city" AS "nppes_provider_city",   "Medicare2_2"."nppes_provider_first_name" AS "nppes_provider_first_name",   "Medicare2_2"."nppes_provider_last_org_name" AS "nppes_provider_last_org_name",   "Medicare2_2"."nppes_provider_street1" AS "nppes_provider_street1",   CAST("Medicare2_2"."nppes_provider_zip" AS BIGINT) AS "nppes_provider_zip",   SUM((CAST("Medicare2_2"."average_Medicare_payment_amt" AS double) * CAST(CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT) AS double))) AS "sum:total_Medicare_payment (copy):ok",   (CAST("Medicare2_2"."average_Medicare_payment_amt" AS double) * CAST(CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT) AS double)) AS "total_Medicare_payment (copy)" FROM "Medicare2_2" WHERE (("Medicare2_2"."nppes_provider_state" = 'NY') AND ("Medicare2_2"."nppes_provider_country" = 'US') AND ("Medicare2_2"."provider_type" = 'Allergy/Immunology')) GROUP BY "Medicare2_2"."bene_unique_cnt",   "Medicare2_2"."hcpcs_code",   3,   "Medicare2_2"."line_srvc_cnt",   5,   6,   7,   8,   "Medicare2_2"."nppes_provider_zip",   11,   1,   2,   4,   9
SELECT CAST("Medicare2_2"."npi" AS BIGINT) AS "npi",   "Medicare2_2"."nppes_credentials" AS "nppes_credentials",   "Medicare2_2"."nppes_provider_city" AS "nppes_provider_city",   "Medicare2_2"."nppes_provider_first_name" AS "nppes_provider_first_name",   "Medicare2_2"."nppes_provider_last_org_name" AS "nppes_provider_last_org_name",   "Medicare2_2"."nppes_provider_street1" AS "nppes_provider_street1",   CAST("Medicare2_2"."nppes_provider_zip" AS BIGINT) AS "nppes_provider_zip",   SUM((CAST("Medicare2_2"."average_Medicare_payment_amt" AS double) * CAST(CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT) AS double))) AS "sum:Calculation_5520413173637078:ok",   SUM(CAST("Medicare2_2"."bene_unique_cnt" AS BIGINT)) AS "sum:bene_unique_cnt:ok",   SUM(CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT)) AS "sum:line_srvc_cnt:ok" FROM "Medicare2_2" WHERE (("Medicare2_2"."nppes_provider_state" = 'NY') AND ("Medicare2_2"."nppes_provider_country" = 'US') AND ("Medicare2_2"."provider_type" = 'Allergy/Immunology')) GROUP BY "Medicare2_2"."npi",   2,   3,   4,   5,   6,   "Medicare2_2"."nppes_provider_zip",   1,   7
SELECT CAST("Medicare2_2"."npi" AS BIGINT) AS "npi",   "Medicare2_2"."nppes_provider_city" AS "nppes_provider_city",   "Medicare2_2"."nppes_provider_first_name" AS "nppes_provider_first_name",   "Medicare2_2"."nppes_provider_last_org_name" AS "nppes_provider_last_org_name",   "Medicare2_2"."provider_type" AS "provider_type",   SUM((CAST("Medicare2_2"."average_Medicare_payment_amt" AS double) * CAST(CAST("Medicare2_2"."line_srvc_cnt" AS BIGINT) AS double))) AS "sum:Calculation_5520413173637078:ok" FROM "Medicare2_2" WHERE ((NOT ("Medicare2_2"."nppes_provider_first_name" IS NULL)) AND ("Medicare2_2"."nppes_provider_state" = 'NY')) GROUP BY "Medicare2_2"."npi",   2,   3,   4,   5,   1
