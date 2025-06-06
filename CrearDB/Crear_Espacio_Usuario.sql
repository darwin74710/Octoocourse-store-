connect system/123

show con_name

ALTER SESSION SET CONTAINER=CDB$ROOT;
ALTER DATABASE OPEN;

DROP TABLESPACE ts_octoocourse INCLUDING CONTENTS and DATAFILES;
    
CREATE TABLESPACE ts_octoocourse LOGGING
DATAFILE 'C:\OracleOctooCourse\DF_octoocourse.dbf' size 100M
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
grant connect, resource,dba to us_admin_octoo; 

connect us_admin_octoo/123

show user

