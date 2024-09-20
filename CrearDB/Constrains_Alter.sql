---SCRIPT PARA ALTERAR LAS TABLAS----
----ASIGNACION DE CONSTRAINT'S------
ALTER TABLE ESTUDIANTES ADD CONSTRAINT
        PK_ESTUDIANTES PRIMARY KEY(ID_ESTUDIANTE);

-------------------------------------------------- 
ALTER TABLE CERTIFICADOS ADD CONSTRAINT
        PK_CERTIFICADOS PRIMARY KEY(ID_CERTIFICADO);
        
-------------------------------------------------- 
ALTER TABLE CURSOS ADD CONSTRAINT
        PK_CURSOS PRIMARY KEY(ID_CURSO);
        
-------------------------------------------------- 
ALTER TABLE CURSOS_APROBADOS ADD CONSTRAINT
        PK_CUR_APROB PRIMARY KEY(ID_CURSO, ID_ESTUDIANTE);
-------------------------------------------------- 
ALTER TABLE CURSOS_FAVORITOS ADD CONSTRAINT
        PK_CUR_FAV PRIMARY KEY(ID_CURSO, NIT);
--------------------------------------------------
ALTER TABLE EMPRESAS ADD CONSTRAINT
        PK_EMPRESAS PRIMARY KEY(NIT);
-------------------------------------------------- 
ALTER TABLE OFERTAS_EMPLEOS ADD CONSTRAINT
        PK_OFERT_EMPLEOS PRIMARY KEY(ID_OFERTA);
-------------------------------------------------- 
ALTER TABLE PRUEBAS_ADMISIONES ADD CONSTRAINT
        PK_PRU_ADMIS PRIMARY KEY(ID_PRUEBA);
-------------------------------------------------- 
ALTER TABLE HOJAS_DE_VIDA ADD CONSTRAINT
        PK_H_VIDA PRIMARY KEY(ID_HOJA_VIDA);
---------------------------------------------------
ALTER TABLE LENGUAJES_PROG ADD CONSTRAINT
        PK_LENGUAJES_PROG PRIMARY KEY(ID_LENGUAJE);
        
------------------------------------------------------
ALTER TABLE APTITUDES ADD CONSTRAINT
        PK_APTITUDES PRIMARY KEY(ID_APTITUDES);

--------------------------------------------------
ALTER TABLE IDIOMAS ADD CONSTRAINT
        PK_IDIOMAS PRIMARY KEY(ID_IDIOMA);

--------------------------------------------------
ALTER TABLE FORMACIONES_ACADEMICAS ADD CONSTRAINT
        PK_FORM_ACADEMICAS PRIMARY KEY(ID_FORMACION);

ALTER TABLE EXP_LABORAL ADD CONSTRAINT
        PK_EXP_LABORAL PRIMARY KEY(ID_EXP);