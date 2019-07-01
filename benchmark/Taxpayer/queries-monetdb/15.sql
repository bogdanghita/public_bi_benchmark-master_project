SELECT AVG(CAST(("Taxpayer_10"."average_Medicare_allowed_amt" - "Taxpayer_10"."average_Medicare_payment_amt") AS double)) AS "avg:Calculation_9940518082838207:ok",   "Taxpayer_10"."nppes_provider_first_name" AS "nppes_provider_first_name" FROM "Taxpayer_10" WHERE (("Taxpayer_10"."hcpcs_description" = 'Initial hospital care') AND ("Taxpayer_10"."nppes_provider_city" IN ('BELLEVUE', 'BELLVUE')) AND ("Taxpayer_10"."nppes_provider_state" = 'WA')) GROUP BY "Taxpayer_10"."nppes_provider_first_name";
