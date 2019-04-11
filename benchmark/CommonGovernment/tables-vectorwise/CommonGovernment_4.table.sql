CREATE TABLE "CommonGovernment_4"(
"Number of Records" smallint NOT NULL,
"a_aid_acontid_agencyid" varchar(4) NOT NULL,
"a_aid_acontid_piid" varchar(50) NOT NULL,
"ag_name" varchar(50) NOT NULL,
"agency_code" varchar(2) NOT NULL,
"ase_rowid" integer NOT NULL,
"award_type" varchar(21) NOT NULL,
"award_type_code" varchar(1) NOT NULL,
"award_type_key" smallint NOT NULL,
"baseandalloptionsvalue" float8 NOT NULL,
"baseandexercisedoptionsvalue" float8 NOT NULL,
"bureau_code" varchar(2) NOT NULL,
"bureau_name" varchar(40) NOT NULL,
"cd_contactiontype" varchar(1),
"co_name" varchar(44),
"co_state" varchar(2),
"code" varchar(2) NOT NULL,
"contract_num" varchar(50),
"contract_signeddate" varchar(20) NOT NULL,
"contractingofficeagencyid" varchar(4) NOT NULL,
"count_fetched" integer NOT NULL,
"count_total" integer NOT NULL,
"description" varchar(40) NOT NULL,
"fk_epa_des_prod" smallint,
"fk_rec_mat" smallint,
"ftsdollar" float8 NOT NULL,
"funding_agency" varchar(4),
"funding_agency_key" integer NOT NULL,
"funding_agency_name" varchar(40) NOT NULL,
"gsadollar" float8 NOT NULL,
"gsaotherdollar" float8 NOT NULL,
"gwacs" float8 NOT NULL,
"level1_category" varchar(37) NOT NULL,
"level2_category" varchar(57) NOT NULL,
"naics_code" varchar(6) NOT NULL,
"naics_name" varchar(35) NOT NULL,
"nongsadollar" float8 NOT NULL,
"obligatedamount" float8 NOT NULL,
"obligatedamount_1" decimal(1, 0),
"pbsdollar" float8 NOT NULL,
"primary_contract_piid" varchar(51) NOT NULL,
"prod_or_serv_code" varchar(4) NOT NULL,
"prod_or_serv_code_desc" varchar(35),
"psc_code" varchar(4) NOT NULL,
"psc_code_description" varchar(100) NOT NULL,
"psc_key" integer NOT NULL,
"quarter" varchar(1) NOT NULL,
"refidvid_agencyid" varchar(4) NOT NULL,
"refidvid_piid" varchar(34),
"short_name" varchar(11) NOT NULL,
"signeddate" varchar(19) NOT NULL,
"vend_contoffbussizedeterm" varchar(1) NOT NULL,
"vend_dunsnumber" varchar(9) NOT NULL,
"vend_vendorname" varchar(108),
"whocanuse" varchar(50),
"year" varchar(4) NOT NULL
);
