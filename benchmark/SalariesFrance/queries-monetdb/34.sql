SELECT SUM(ABS("SalariesFrance_13"."EMBAUCHE_CDI")) AS "TEMP(Calculation_369576668387979265)(1183172592)(0)",   SUM(ABS("SalariesFrance_13"."EMBAUCHE_CDI")) AS "TEMP(Calculation_369576668387979265)(1291741352)(0)",   SUM(ABS("SalariesFrance_13"."EMBAUCHE_CDD")) AS "TEMP(Calculation_369576668387979265)(3218284358)(0)",   SUM(ABS("SalariesFrance_13"."INTERIM_NP1")) AS "TEMP(Calculation_369576668387979265)(4177782722)(0)",   SUM(ABS("SalariesFrance_13"."BMO_DIFFICILE")) AS "TEMP(Calculation_369576668391063555)(1826962959)(0)",   SUM(ABS("SalariesFrance_13"."BMO_INTENTIONS")) AS "TEMP(Calculation_369576668391063555)(2306732790)(0)",   SUM("SalariesFrance_13"."BMO_INTENTIONS") AS "TEMP(Calculation_369576668391063555)(4168827534)(0)",   SUM("SalariesFrance_13"."EMPSAL_NP1") AS "TEMP(Calculation_369576668395024390)(2478313272)(0)",   SUM("SalariesFrance_13"."AG_M25") AS "TEMP(Calculation_369576668395024390)(3700677619)(0)",   SUM("SalariesFrance_13"."FEMMES") AS "TEMP(Calculation_369576668396457992)(2123450049)(0)",   SUM("SalariesFrance_13"."EMPSAL_NP1") AS "TEMP(Calculation_369576668396457992)(3149183137)(0)",   SUM("SalariesFrance_13"."SALAIRE_VF") AS "TEMP(Calculation_393783518251319297)(57485518)(0)",   COUNT("SalariesFrance_13"."SALAIRE_VF") AS "TEMP(Calculation_393783518251319297)(879651027)(0)",   SUM("SalariesFrance_13"."AG_30_39") AS "TEMP(Entre 25 et 29 ans (copie))(3219587110)(0)",   SUM(("SalariesFrance_13"."AG_40_49" + "SalariesFrance_13"."AG_50_54")) AS "TEMP(Entre 30 et 39 ans (copie))(3826808445)(0)",   SUM("SalariesFrance_13"."AG_P55") AS "TEMP(Moins de 25 ans (copie 2))(3051566802)(0)",   SUM("SalariesFrance_13"."AG_25_29") AS "TEMP(Moins de 25 ans (copie))(341663134)(0)",   SUM("SalariesFrance_13"."HOMMES") AS "TEMP(des femmes (copie))(64173573)(0)",   AVG(CAST(CAST("SalariesFrance_13"."Calculation_163536984210948109" AS BIGINT) AS double)) AS "avg:Calculation_163536984210948109:ok",   AVG(CAST(CAST("SalariesFrance_13"."REPERE1 (copie)" AS BIGINT) AS double)) AS "avg:REPERE1 (copie):ok",   CAST(MIN("SalariesFrance_13"."Calculation_163536984210948109") AS BIGINT) AS "min:Calculation_163536984210948109:ok",   CAST(MIN("SalariesFrance_13"."REPERE1 (copie)") AS BIGINT) AS "min:REPERE1 (copie):ok" FROM "SalariesFrance_13" WHERE ("SalariesFrance_13"."REG_LIB" = 'NOUVELLE-AQUITAINE') HAVING (COUNT(1) > 0);
