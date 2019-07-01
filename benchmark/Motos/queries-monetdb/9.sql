SELECT "Motos_2"."Marca" AS "Datos (copia)",   "Motos_2"."Medio" AS "Medio",   SUM("Motos_2"."InversionUS") AS "sum:Calculation_0061002123102817:ok" FROM "Motos_2" WHERE (("Motos_2"."Categoria" IN ('CAMIONES', 'CAMIONES, BUSES Y PANELES', 'MOTOCICLETAS', 'PICK UPS, VANS Y JEEPS', 'PICK-UPS', 'SUV Y JEEPS', 'VEHICULOS NUEVOS')) AND (CAST(EXTRACT(YEAR FROM "Motos_2"."FECHA") AS BIGINT) >= 2010) AND (CAST(EXTRACT(YEAR FROM "Motos_2"."FECHA") AS BIGINT) <= 2015) AND ("Motos_2"."Categoria" = 'MOTOCICLETAS')) GROUP BY "Motos_2"."Marca",   "Motos_2"."Medio";
