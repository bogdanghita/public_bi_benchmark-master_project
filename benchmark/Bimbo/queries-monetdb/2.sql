SELECT CAST("Bimbo_1"."Demanda_uni_equil" AS BIGINT) AS "Demanda_uni_equil",   CAST("Bimbo_1"."Venta_uni_hoy" AS BIGINT) AS "Venta_uni_hoy" FROM "Bimbo_1" WHERE (CAST("Bimbo_1"."Agencia_ID" AS BIGINT) IN (1110, 1111, 1112, 1113, 1114, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1126, 1127, 1129, 1130, 1137, 1138)) GROUP BY "Bimbo_1"."Demanda_uni_equil",   "Bimbo_1"."Venta_uni_hoy",   "Demanda_uni_equil",   "Bimbo_1"."Venta_uni_hoy";
