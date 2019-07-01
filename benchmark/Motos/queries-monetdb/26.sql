SELECT SUM("Motos_2"."InversionUS") AS "sum:Calculation_0061002123102817:ok",   SUM("Motos_2"."InversionUS") AS "sum:InversionUS:ok",   CAST(EXTRACT(YEAR FROM "Motos_2"."FECHA") AS BIGINT) AS "yr:FECHA:ok" FROM "Motos_2" WHERE ((CAST(EXTRACT(YEAR FROM "Motos_2"."FECHA") AS BIGINT) >= 2010) AND (CAST(EXTRACT(YEAR FROM "Motos_2"."FECHA") AS BIGINT) <= 2015) AND ("Motos_2"."Categoria" IN ('CAMIONES', 'CAMIONES, BUSES Y PANELES', 'MOTOCICLETAS', 'PICK UPS, VANS Y JEEPS', 'PICK-UPS', 'SUV Y JEEPS', 'VEHICULOS NUEVOS')) AND ("Motos_2"."Categoria" = 'MOTOCICLETAS') AND ("Motos_2"."Marca" IN ('MOTOCICLETAS YAMAHA', 'YAMAHA')) AND (CAST(EXTRACT(MONTH FROM "Motos_2"."FECHA") AS BIGINT) >= 1) AND (CAST(EXTRACT(MONTH FROM "Motos_2"."FECHA") AS BIGINT) <= 9)) GROUP BY "yr:FECHA:ok";
