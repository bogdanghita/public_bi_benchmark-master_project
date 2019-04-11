CREATE TABLE "Rentabilidad_2"(
"AUTOPREVENTA: Costo Fijo" decimal(18, 12) NOT NULL,
"AUTOPREVENTA: Costo Variable" float8 NOT NULL,
"AUTOPREVENTA: Costo de Devoluciones" float8 NOT NULL,
"AUTOPREVENTA: Tiempos de Venta + Traslado Autopreventa Normal" decimal(18, 14) NOT NULL,
"AUTOVENTA: Carga Paseante" float8 NOT NULL,
"AUTOVENTA: Costo Fijo" float8 NOT NULL,
"AUTOVENTA: Costo Variable" float8 NOT NULL,
"AUTOVENTA: Tiempos de Venta + Traslado Autoventa Normal" decimal(17, 14) NOT NULL,
"BODEGA: CEDIS Propio- Costos Bodega" float8 NOT NULL,
"BODEGA: Costo Arriendo Terceros" float8 NOT NULL,
"BODEGA: Costo Especialistas de Operaciones" varchar(1),
"BODEGA: Distribuidores- Costos Fijos y Variables" float8 NOT NULL,
"BODEGA: Mermas" varchar(1),
"CF" float8 NOT NULL,
"CU" float8 NOT NULL,
"Calle" varchar(62),
"Canal de Ventas" smallint NOT NULL,
"Ciudad UO" varchar(15) NOT NULL,
"Descripción de Canal" varchar(47),
"Deudor NCB" integer,
"Deudor" integer NOT NULL,
"Dias de Visita CO" varchar(6),
"Dias de Visita TA NCB" varchar(1),
"Dias de Visita TA" varchar(6),
"Días de Entrega" varchar(6),
"Días de Visita PR NCB" varchar(6),
"Días de Visita PR" varchar(6),
"Dïas de Entrega NCB" varchar(6),
"Figura Especifica" varchar(27),
"Figura" varchar(29) NOT NULL,
"Fijo / Dinámica" varchar(8) NOT NULL,
"Fx CO" smallint,
"Fx Entrega Total NCB" smallint,
"Fx Entrega Total" smallint,
"Fx PR NCB" smallint,
"Fx PR" smallint,
"Fx TA NCB" varchar(1),
"Fx TA" smallint,
"FxED" smallint,
"GEC NCB" varchar(2),
"GEC" varchar(2) NOT NULL,
"GERENTES VENTA: Coordinadores Bronces" decimal(17, 11) NOT NULL,
"GERENTES VENTA: Costo Gerente de Ventas Normal" decimal(18, 11) NOT NULL,
"GUC" varchar(3) NOT NULL,
"Gerencia" varchar(4) NOT NULL,
"IN" float8 NOT NULL,
"Implementación Venta" varchar(12) NOT NULL,
"Jefatura de Reparto NCB" varchar(4),
"Jefatura de Reparto" varchar(4) NOT NULL,
"Jefe de Ventas NCB" varchar(3),
"Jefe de Ventas" varchar(3) NOT NULL,
"Latitud AUTO PREV" decimal(16, 14),
"Latitud" varchar(14),
"Locación" varchar(15) NOT NULL,
"Longitud AUTO PREV" decimal(15, 13),
"Longitud" varchar(15),
"MATCH PR con NCB" varchar(5),
"MERCADEO: Costo Refrigeración" decimal(18, 11) NOT NULL,
"MERCADEO: PDE" decimal(17, 11) NOT NULL,
"MERCADEO: PDV- Descuentos Habituales" integer NOT NULL,
"MERCADEO: PDV- Descuentos No Habituales" integer NOT NULL,
"MERCADEO: Prorrateo Mercaderistas" float8 NOT NULL,
"Modalidad de Venta" varchar(18) NOT NULL,
"Modalidad reparto" varchar(18) NOT NULL,
"Municipio" varchar(49),
"NCB" varchar(3),
"NIT" varchar(16),
"Nombre del Cliente" varchar(48),
"Number of Records" smallint NOT NULL,
"ON-OFF" varchar(2),
"OP. DISTRIBUIDORES: Costo Fijo" float8 NOT NULL,
"OP. DISTRIBUIDORES: Costo Variable" float8 NOT NULL,
"OP. DISTRIBUIDORES: Filtro de Validación Costo Variable" varchar(2) NOT NULL,
"OP. DISTRIBUIDORES: Mayoristas" float8 NOT NULL,
"OP. DISTRIBUIDORES: NO GVF" float8 NOT NULL,
"OP. DISTRIBUIDORES: Prorrateo Visitas" float8 NOT NULL,
"OTROS VENTA: Costo de Rotación Pre/Televendedores" decimal(16, 12),
"PREVENTA NCB: Costo de Prevendedor NCB" float8,
"PREVENTA NCB: Tiempos de Venta + Traslado Preventa NCB" decimal(16, 14),
"PREVENTA: Costo de Prevendedor Normal" float8 NOT NULL,
"PREVENTA: Tiempos de Venta + Traslado Preventa Normal" decimal(17, 14) NOT NULL,
"Población Distribuidor GVF/GVI" varchar(21) NOT NULL,
"Precio Prom. CF" float8 NOT NULL,
"Precio Prom. CU" float8 NOT NULL,
"REPARTO: Costo Supervisores" float8 NOT NULL,
"REPARTO: Costo de Bodegas Secundarias" float8 NOT NULL,
"REPARTO: Costo de Depreciación" float8 NOT NULL,
"REPARTO: Costo de Mantenimiento" float8 NOT NULL,
"REPARTO: Devoluciones" float8 NOT NULL,
"REPARTO: Merma de Ruta" float8 NOT NULL,
"REPARTO: Rutas Dinamicas- Costos Fijos" float8 NOT NULL,
"REPARTO: Rutas Dinamicas- Costos Variables" float8 NOT NULL,
"REPARTO: Rutas Fijas- Costos Fijos" float8 NOT NULL,
"REPARTO: Rutas Fijas- Costos Variables" float8 NOT NULL,
"REPARTO: Tiempos de Reparto Fijo + Variable" decimal(18, 13) NOT NULL,
"REPARTO: Visitas de Reparto Acumulado Ene-May" smallint NOT NULL,
"Razón Social" varchar(40),
"Rentabilidad" float8 NOT NULL,
"Ruta CO" varchar(6),
"Ruta ED" varchar(6),
"Ruta PR NCB" varchar(6),
"Ruta PR" varchar(6),
"Ruta TA NCB" varchar(6),
"Ruta TA" varchar(6),
"Ruta de Reparto NCB" varchar(8),
"Ruta de Reparto" varchar(6) NOT NULL,
"Ruta de Venta NCB" varchar(6),
"Ruta de Venta" varchar(6) NOT NULL,
"SEDE FORANEO SINTEC" varchar(7) NOT NULL,
"Sede/Foráneo" varchar(7) NOT NULL,
"T1: Cedis Propio" float8 NOT NULL,
"T1: Distruidor Tercero" float8 NOT NULL,
"TELEVENTA OFIC: Costo Televendedor Normal" varchar(1),
"TELEVENTA OFIC: Tiempos de Venta" varchar(1),
"TELEVENTA: Costo Televendedor NCB" smallint,
"TELEVENTA: Costo de Televendedor Normal" float8 NOT NULL,
"TELEVENTA: Tiempos de Venta Televenta NCB" smallint,
"TELEVENTA: Tiempos de Venta Televenta Normal" decimal(16, 14) NOT NULL,
"TOTAL BODEGA C/ARRIENDOS" float8 NOT NULL,
"TOTAL MERCADEO" float8 NOT NULL,
"TOTAL REPARTO" float8 NOT NULL,
"TOTAL T1" float8 NOT NULL,
"TOTAL VENTA" float8 NOT NULL,
"Total CdS" float8 NOT NULL,
"Tradicional/ Moderno" varchar(11) NOT NULL,
"UO" varchar(4) NOT NULL,
"Util. Bruta" float8 NOT NULL,
"VENTA:  MERMA DE VENTA" float8 NOT NULL,
"VENTA: Coord, OL, Merc. 14" integer NOT NULL,
"VENTA: Costo Renta Equipo Televenta NCB" smallint,
"VENTA: Costo Renta de Equipo Televenta Normal" decimal(18, 12) NOT NULL,
"VENTA: Costo Total Mercaderistas" decimal(15, 11) NOT NULL,
"VENTA: Costo de Handheld Rutas Autoventa" float8 NOT NULL,
"VENTA: Costo de Handheld Rutas NCBs" decimal(15, 11),
"VENTA: Costo de Handheld Rutas Preventa" float8 NOT NULL,
"VENTA: Costos EDI" decimal(16, 10) NOT NULL,
"VENTA: Descuentos Lista de Precios" integer NOT NULL,
"Zona" varchar(2) NOT NULL
);
