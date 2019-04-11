CREATE TABLE "NYC_2"(
"Address Type" varchar(12),
"Agency Name" varchar(91) NOT NULL,
"Agency" varchar(10) NOT NULL,
"Borough" varchar(13) NOT NULL,
"Bridge Highway Direction" varchar(30),
"Bridge Highway Name" varchar(42),
"Bridge Highway Segment" date,
"City" varchar(32),
"Closed Date" timestamp,
"Community Board" varchar(25) NOT NULL,
"Complaint Type" varchar(41) NOT NULL,
"Created Date" timestamp NOT NULL,
"Cross Street 1" varchar(36),
"Cross Street 2" varchar(36),
"Descriptor" varchar(82),
"Due Date" timestamp,
"Facility Type" varchar(15),
"Ferry Direction" varchar(19),
"Ferry Terminal Name" varchar(95),
"Garage Lot Name" varchar(27),
"Incident Address" varchar(96),
"Incident Zip" bigint,
"Intersection Street 1" varchar(38),
"Intersection Street 2" varchar(47),
"Landmark" varchar(33),
"Latitude" decimal(15, 13),
"Location Type" varchar(36),
"Location" varchar(40),
"Longitude" decimal(15, 13),
"Number of Records" smallint NOT NULL,
"Park Borough" varchar(13) NOT NULL,
"Park Facility Name" varchar(95) NOT NULL,
"Resolution Action Updated Date" timestamp,
"Resolution Description" varchar(500),
"Road Ramp" varchar(7),
"School Address" varchar(120),
"School City" varchar(19) NOT NULL,
"School Code" varchar(11),
"School Name" varchar(95) NOT NULL,
"School Not Found" varchar(1),
"School Number" varchar(11),
"School Phone Number" varchar(11) NOT NULL,
"School Region" varchar(11),
"School State" varchar(11) NOT NULL,
"School Zip" varchar(11) NOT NULL,
"School or Citywide Complaint" varchar(18),
"Status" varchar(28) NOT NULL,
"Street Name" varchar(96),
"Taxi Company Borough" varchar(13),
"Taxi Pick Up Location" varchar(27),
"Unique Key" integer NOT NULL,
"Vehicle Type" varchar(23),
"X Coordinate (State Plane)" integer,
"Y Coordinate (State Plane)" integer
);
