CREATE TABLE "Redfin3_1"(
"Number of Records" smallint NOT NULL,
"avg_sale_to_list" decimal(16, 15),
"avg_sale_to_list_mom" float8,
"avg_sale_to_list_yoy" float8,
"city" varchar(31),
"homes_sold" integer,
"homes_sold_mom" float8,
"homes_sold_yoy" float8,
"inventory" integer,
"inventory_mom" float8,
"inventory_yoy" float8,
"median_dom" decimal(5, 1),
"median_dom_mom" decimal(5, 1),
"median_dom_yoy" decimal(5, 1),
"median_list_ppsf" float8,
"median_list_ppsf_mom" float8,
"median_list_ppsf_yoy" float8,
"median_list_price" float8,
"median_list_price_mom" float8,
"median_list_price_yoy" float8,
"median_ppsf" float8,
"median_ppsf_mom" float8,
"median_ppsf_yoy" float8,
"median_sale_price" float8,
"median_sale_price_mom" float8,
"median_sale_price_yoy" float8,
"months_of_supply" decimal(5, 1),
"months_of_supply_mom" float8,
"months_of_supply_yoy" float8,
"new_listings" integer,
"new_listings_mom" float8,
"new_listings_yoy" float8,
"period_begin" date NOT NULL,
"period_duration" smallint NOT NULL,
"period_end" date NOT NULL,
"price_drops" float8,
"price_drops_mom" float8,
"price_drops_yoy" float8,
"property_type" varchar(25) NOT NULL,
"region" varchar(75) NOT NULL,
"region_type" varchar(12) NOT NULL,
"sold_above_list" float8,
"sold_above_list_mom" float8,
"sold_above_list_yoy" float8,
"state" varchar(14),
"state_code" varchar(2),
"table_id" integer
);