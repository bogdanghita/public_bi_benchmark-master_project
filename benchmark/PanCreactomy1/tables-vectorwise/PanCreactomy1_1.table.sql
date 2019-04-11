CREATE TABLE "PanCreactomy1_1"(
"AVERAGE_MEDICARE_ALLOWED_AMT" float8,
"AVERAGE_MEDICARE_PAYMENT_AMT" float8,
"AVERAGE_SUBMITTED_CHRG_AMT" float8,
"BENE_DAY_SRVC_CNT" integer,
"BENE_UNIQUE_CNT" integer,
"HCPCS_CODE" varchar(5),
"HCPCS_DESCRIPTION" varchar(255),
"HCPCS_DRUG_INDICATOR" varchar(1),
"LINE_SRVC_CNT" float8,
"MEDICARE_PARTICIPATION_INDICATOR" varchar(1),
"NPI" integer NOT NULL,
"NPPES_CREDENTIALS" varchar(20),
"NPPES_ENTITY_CODE" varchar(1),
"NPPES_PROVIDER_CITY" varchar(28),
"NPPES_PROVIDER_COUNTRY" varchar(2),
"NPPES_PROVIDER_FIRST_NAME" varchar(20),
"NPPES_PROVIDER_GENDER" varchar(1),
"NPPES_PROVIDER_LAST_ORG_NAME" varchar(70),
"NPPES_PROVIDER_MI" varchar(1),
"NPPES_PROVIDER_STATE" varchar(2),
"NPPES_PROVIDER_STREET1" varchar(55),
"NPPES_PROVIDER_STREET2" varchar(55),
"NPPES_PROVIDER_ZIP" integer,
"Number of Records" smallint NOT NULL,
"PLACE_OF_SERVICE" varchar(1),
"PROVIDER_TYPE" varchar(43),
"STDEV_MEDICARE_ALLOWED_AMT" float8,
"STDEV_MEDICARE_PAYMENT_AMT" float8,
"STDEV_SUBMITTED_CHRG_AMT" float8
);
