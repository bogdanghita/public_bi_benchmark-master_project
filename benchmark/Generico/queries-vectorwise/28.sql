SELECT (CASE WHEN ("Generico_5"."Medio" IN ('PRENSA', 'REVISTAS', 'REVISTAS DE PRENSA')) THEN 'PRENSA' ELSE "Generico_5"."Medio" END) AS "Medio (grupo)" FROM "Generico_5" WHERE (("Generico_5"."Anunciante" IN ('BANTRAB/TODOTICKET', 'TODOTICKET', 'TODOTICKET.COM')) AND (CAST(EXTRACT(YEAR FROM "Generico_5"."FECHA") AS BIGINT) >= 2010) AND (CAST(EXTRACT(YEAR FROM "Generico_5"."FECHA") AS BIGINT) <= 2015) AND (CAST(EXTRACT(YEAR FROM "Generico_5"."FECHA") AS BIGINT) = 2015)) GROUP BY 1;