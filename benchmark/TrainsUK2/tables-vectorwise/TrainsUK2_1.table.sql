CREATE TABLE "TrainsUK2_1"(
"Actual Total Distance Miles" decimal(5, 2),
"Date" timestamp,
"Financial Year & Period" varchar(23),
"Number of Records" smallint NOT NULL,
"Operator" varchar(8),
"Planned Dest Actual Datetime" timestamp,
"Planned Dest GBTT Datetime" timestamp,
"Planned Dest Stanox Description" varchar(31),
"Planned Dest Stanox" integer,
"Planned Dest WTT Datetime" timestamp,
"Planned Orig Stanox Description" varchar(31),
"Planned Orig Stanox" integer,
"Planned Origin Actual Datetime" timestamp,
"Planned Origin GBTT Datetime" timestamp,
"Planned Origin WTT Datetime" timestamp,
"Planned Total Distance Miles" decimal(5, 2),
"Service Group Code" varchar(18),
"Service Group Description" varchar(42),
"TSC" integer,
"Train ID" varchar(10),
"v_CaSL Flag" smallint NOT NULL,
"v_Dest Lateness (GBTT)" smallint,
"v_Dest Lateness (WTT)" decimal(4, 1),
"v_Full Cancellation Flag" smallint NOT NULL,
"v_Origin Lateness (GBTT)" smallint,
"v_Origin Lateness (WTT)" smallint,
"v_PPM Pass Flag" smallint NOT NULL,
"v_RT Flag" smallint NOT NULL,
"v_Sector" varchar(8),
"v_Unique Train ID" varchar(24),
"c_Origin Time (GBTT) (copy)" varchar(5),
"Calculation_2510610113130467" smallint,
"Calculation_4220604162631191" varchar(71),
"Calculation_5580608170646388" varchar(5),
"Calculation_6080608165132814" varchar(4),
"Calculation_9230610113105724" smallint,
"Date (group)" timestamp
);
