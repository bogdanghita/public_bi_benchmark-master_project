--SELECT "Food_1"."device" AS "device",   SUM("Food_1"."Calculation_1553038251895332871") AS "sum:Calculation_1553038251895332871:ok" FROM "Food_1" WHERE ("Food_1"."vendor" = 'Apple') GROUP BY 1;
