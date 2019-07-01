--SELECT "TableroSistemaPenal_1"."Calculation_3100811173420213" AS "Calculation_3100811173420213",   "TableroSistemaPenal_1"."Calculation_5590723164209972" AS "Calculation_5590723164209972",   AVG(CAST("TableroSistemaPenal_1"."DURACIÓN" AS float8)) AS "avg:DURACIÓN:ok",   CAST(EXTRACT(YEAR FROM DATETIME("TableroSistemaPenal_1"."FEC_TERMINO")) AS BIGINT) AS "yr:FEC_TERMINO:ok" FROM "TableroSistemaPenal_1" WHERE ((("TableroSistemaPenal_1"."MOT_TERMINO" >= 'ABANDONO DE LA QUERELLA') AND ("TableroSistemaPenal_1"."MOT_TERMINO" <= 'APROBACIÓN NO INICIO INVESTIGACIÓN.')) OR (("TableroSistemaPenal_1"."MOT_TERMINO" >= 'COMUNICA Y/O APLICA DECISIÓN PPIO. DE OPORTUNIDAD.') AND ("TableroSistemaPenal_1"."MOT_TERMINO" <= 'SENTENCIA CONDENATORIA'))) GROUP BY 1,   2,   4;
