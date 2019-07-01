CREATE TABLE "Taxpayer_9"(
"Number of Records" smallint NOT NULL,
"average_Medicare_allowed_amt" float8,
"average_Medicare_payment_amt" float8,
"average_submitted_chrg_amt" float8,
"bene_day_srvc_cnt" integer,
"bene_unique_cnt" integer,
"hcpcs_code" integer,
"hcpcs_description" varchar(28),
"line_srvc_cnt" integer,
"medicare_participation_indicator" varchar(1),
"npi" integer NOT NULL,
"nppes_credentials" varchar(20),
"nppes_entity_code" varchar(1),
"nppes_provider_city" varchar(28),
"nppes_provider_country" varchar(2),
"nppes_provider_first_name" varchar(20),
"nppes_provider_gender" varchar(1),
"nppes_provider_last_org_name" varchar(70),
"nppes_provider_mi" varchar(1),
"nppes_provider_state" varchar(2),
"nppes_provider_street1" varchar(55),
"nppes_provider_street2" varchar(55),
"nppes_provider_zip" integer,
"place_of_service" varchar(1),
"provider_type" varchar(43),
"stdev_Medicare_allowed_amt" float8,
"stdev_Medicare_payment_amt" float8,
"stdev_submitted_chrg_amt" float8
);
