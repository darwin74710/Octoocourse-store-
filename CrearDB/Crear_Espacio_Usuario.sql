connect system/123

show con_name

ALTER SESSION SET CONTAINER=CDB$ROOT;
ALTER DATABASE OPEN;

DROP TABLESPACE ts_octoocourse INCLUDING CONTENTS and DATAFILES;
    
CREATE TABLESPACE ts_octoocourse LOGGING
DATAFILE 'C:\Users\zTMike\Desktop\Semestre3\BaseDeDatos\Bases\lamarquesa.dbf' size 1M
extent management local segment space management auto; 
 
alter session set "_ORACLE_SCRIPT"=true; 
 
drop user us_admin_octoo cascade;
SELECT tablespace_name FROM dba_tablespaces WHERE tablespace_name = 'ts_octoocourse';
    
CREATE user us_admin_octoo profile 
default identified by 123
default tablespace ts_octoocourse 
temporary tablespace temp 
account unlock;     

--privilegios
grant connect, resource,dba to ts_octoocourse; 

connect ts_octoocourse/123

show user

