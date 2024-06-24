1. Lo primero que hice fue crear las tablas con sus requerimientos:
   
CREATE TABLE HUB_Fisico ( Usuario VARCHAR, IdStock INTEGER, Descrip
VARCHAR(255), Apto VARCHAR, Terminal VARCHAR, TS TIMESTAMP );
CREATE TABLE SAT_Stocks ( Idb INTEGER, Id INTEGER, Scanning INTEGER, UxB
INTEGER, IdStock INTEGER, CantStock INTEGER, Unidades INTEGER, Usuario
VARCHAR, Terminal VARCHAR, TS TIMESTAMP
CREATE TABLE Link ( IdStock INTEGER, idarticulo INTEGER, TS TIMESTAMP );
CREATE TABLE HUB_post ( Id INTEGER, idarticulo INTEGER, idnumero INTEGER, Mna
VARCHAR, SectSecc INTEGER, Usuario VARCHAR, Terminal VARCHAR, TS
TIMESTAMP, CodigoSap INTEGER );
CREATE TABLE SAT_final ( Mna VARCHAR, idarticulo INTEGER, Descrip VARCHAR,
TipoCotizacion VARCHAR, Terminal VARCHAR, Usuario VARCHAR, TS TIMESTAMP );

3. Luego de crear las tablas, le pedí a la IA que me genere datos aleatorios para
poder interactuar con las consultas SQL:

4. “SQL que genere como resultado la información de cuál fue la foto del stock el día
anterior. Esto debe ser realizado por la llave de negocio correspondiente”. La
consulta que realice fue la siguiente:
SELECT
 HUB_fisico.Usuario, HUB_fisico.IdStock,
 HUB_fisico.Descrip, HUB_fisico.Apto,
 HUB_fisico.Terminal, HUB_fisico.TS AS Foto
FROM
 HUB_Fisico
JOIN
 SAT_Stocks ON HUB_Fisico.IdStock = SAT_Stocks.IdStock
WHERE
 DATE(HUB_Fisico.TS) = CURRENT_DATE – INTERVAL ‘1 day’;
Dado a que los datos eran de la fecha de hoy probe la consulta sin “INTERVAL ‘1
day” para confirmar si funcionaba, efectivamente, funcionó:

![image](https://github.com/carromarco/Data-And-Science/assets/117318209/7d99dd9c-da11-4033-b2af-b8ddd98d61b6)

Luego de eso, inserte nuevos datos a mis tablas para que la consulta anterior
funcione: 

![image](https://github.com/carromarco/Data-And-Science/assets/117318209/6fc30f20-625e-4ce2-ad4f-a48764409539)

Datamart para proveedores:
CREATE SCHEMA PROVEEDORES;
CREATE TABLE PROVEEDORES.Distr (Empresa varchar, TS timestamp, mail
varchar);
Cargue datos aleatorios para los proveedores: 

![image](https://github.com/carromarco/Data-And-Science/assets/117318209/9eb2af12-e378-4887-a999-7306417d3b2e)

