---SCRIPT PARA BORRAR LAS TABLAS---
DROP TABLE ESTUDIANTES;
DROP TABLE CURSOS;
DROP TABLE CERTIFICADOS;
DROP TABLE CURSOS_APROBADOS;
DROP TABLE  EMPRESAS;
DROP TABLE  OFERTAS_EMPLEOS;
DROP TABLE  HOJAS_DE_VIDA;
DROP TABLE  LENGUAJES_PROG;
DROP TABLE  APTITUDES;
DROP TABLE  IDIOMAS;
DROP TABLE  FORMACIONES_ACADEMICAS;
DROP TABLE  EXP_LABORALES;



CREATE TABLE ESTUDIANTES(
  ID_ESTUDIANTE NUMBER(10),
  TIPO_ID VARCHAR2(25),
  NOM_ESTUDIANTE VARCHAR2(50),
  APELLIDO VARCHAR2(50),
  CORREO_ESTUDIANTE VARCHAR2(50),
  FECHA_NAC DATE,
  PASSWORD_ESTUDIANTE VARCHAR2(255),
  CONSTRAINT PK_ESTUDIANTE PRIMARY KEY (ID_ESTUDIANTE)
);

-------------------------------
CREATE TABLE CURSOS (
  ID_CURSO NUMBER(10),
  NOM_CURSO CHAR(50),
  DIFICULTAD CHAR(10),
  DESCRIPCION VARCHAR2(1000),
  ID_ESTUDIANTE NUMBER(10),
  CONSTRAINT PK_CURSO PRIMARY KEY (ID_CURSO),
  CONSTRAINT FK_CURSO_ESTUDIANTE FOREIGN KEY (ID_ESTUDIANTE) REFERENCES ESTUDIANTES(ID_ESTUDIANTE)
);

-------------------------------
CREATE TABLE CERTIFICADOS (
  ID_CERTIFICADO NUMBER(10),
  ID_ESTUDIANTE NUMBER(10),
  ID_CURSO NUMBER(10),
  CONSTRAINT PK_CERTIFICADO PRIMARY KEY (ID_CERTIFICADO),
  CONSTRAINT FK_CERTIFICADO_ESTUDIANTE FOREIGN KEY (ID_ESTUDIANTE) REFERENCES ESTUDIANTES(ID_ESTUDIANTE),
  CONSTRAINT FK_CERTIFICADO_CURSO FOREIGN KEY (ID_CURSO) REFERENCES CURSOS(ID_CURSO)
);

-------------------------------
CREATE TABLE CURSOS_APROBADOS (
  ID_APROBADO NUMBER(10),
  ID_CURSO NUMBER(10),
  ID_ESTUDIANTE NUMBER(10),
  CONSTRAINT PK_APROBADO PRIMARY KEY (ID_APROBADO),
  CONSTRAINT FK_APROBADOS_CURSO FOREIGN KEY (ID_CURSO) REFERENCES CURSOS(ID_CURSO),
  CONSTRAINT FK_APROBADOS_ESTUDIANTE FOREIGN KEY (ID_ESTUDIANTE) REFERENCES ESTUDIANTES(ID_ESTUDIANTE)
);

-------------------------------
CREATE TABLE EMPRESAS (
  NIT NUMBER(25),
  NOM_EMPRESA VARCHAR2(50),
  DIRECCION VARCHAR2(60),
  CORREO_EMP VARCHAR2(50),
  PASSWORD_EMP VARCHAR2(255),
  TELEFONO NUMBER(10),
  CONSTRAINT PK_EMPRESA PRIMARY KEY (NIT)
);

-------------------------------

CREATE TABLE OFERTAS_EMPLEOS (
  ID_OFERTA        NUMBER(10)  NOT NULL,
  NIT              NUMBER(25),
  NOMBRE_OFERTA    VARCHAR2(50),
  SALARIO          NUMBER(15, 2),  
  DESCRIPCION      VARCHAR2(1000),
  CONSTRAINT PK_OFERTA PRIMARY KEY (ID_OFERTA),
  CONSTRAINT FK_OFERTA_EMPRESA FOREIGN KEY (NIT) REFERENCES EMPRESAS(NIT)
);

//agregue estado
alter table ofertas_empleos
add ( ESTADO NUMBER(1));

alter table ofertas_empleos
add ( FECHA_PUB DATE);
-------------------------------

CREATE TABLE CONOCIMIENTOS(
  ID_CONOCIMIENTO NUMBER(10) PRIMARY KEY,
  ID_OFERTA NUMBER(10),
  NOM_CON VARCHAR2(100),
  CONSTRAINT FK_CONOCIMIENTOS FOREIGN KEY (ID_OFERTA) REFERENCES OFERTAS_EMPLEOS(ID_OFERTA)
);


CREATE TABLE TIPO_CONT(
  ID_TIPO_CONT NUMBER(10),
  ID_OFERTA NUMBER(10),
  CONSTRAINT PK_TIPO_CONT PRIMARY KEY (ID_TIPO_CONT, ID_OFERTA), 
  CONSTRAINT FK_TIPO_CONT FOREIGN KEY (ID_OFERTA) REFERENCES OFERTAS_EMPLEOS(ID_OFERTA)
);

alter table tipo_cont
add ( TIPO_CONT VARCHAR2(50));
-------------------------------
CREATE TABLE HOJAS_DE_VIDA (
  ID_HOJA_VIDA NUMBER(10),
  ID_ESTUDIANTE NUMBER(10),
  DESCRIPCION VARCHAR2(1000),
  TELEFONO NUMBER(10),
  DIRECCION CHAR(60),
  CONSTRAINT PK_HOJA_VIDA PRIMARY KEY (ID_HOJA_VIDA),
  CONSTRAINT FK_HOJA_VIDA_ESTUDIANTE FOREIGN KEY (ID_ESTUDIANTE) REFERENCES ESTUDIANTES(ID_ESTUDIANTE)
);

------------------------------
CREATE TABLE LENGUAJES_PROG (
  ID_LENGUAJE NUMBER(10),
  ID_HOJAVIDA NUMBER(10),
  NOMBRE_LENG CHAR(50),
  CONSTRAINT PK_LENGUAJE PRIMARY KEY (ID_LENGUAJE),
  CONSTRAINT FK_LENGUAJE_HOJA_VIDA FOREIGN KEY (ID_HOJAVIDA) REFERENCES HOJAS_DE_VIDA(ID_HOJA_VIDA)
);

-------------------------------
CREATE TABLE APTITUDES (
  ID_APTITUDES NUMBER(10),
  ID_HOJAVIDA NUMBER(10),
  NOMBRE_APT CHAR(50),
  CONSTRAINT PK_APTITUDES PRIMARY KEY (ID_APTITUDES),
  CONSTRAINT FK_APTITUDES_HOJA_VIDA FOREIGN KEY (ID_HOJAVIDA) REFERENCES HOJAS_DE_VIDA(ID_HOJA_VIDA)
);
-------------------------------
CREATE TABLE IDIOMAS (
  ID_IDIOMA NUMBER(10),
  ID_HOJAVIDA NUMBER(10),
  IDIOMA CHAR(20),
  NIVEL CHAR(20),
  CONSTRAINT PK_IDIOMA PRIMARY KEY (ID_IDIOMA),
  CONSTRAINT FK_IDIOMA_HOJA_VIDA FOREIGN KEY (ID_HOJAVIDA) REFERENCES HOJAS_DE_VIDA(ID_HOJA_VIDA)
);

-------------------------------
CREATE TABLE FORMACIONES_ACADEMICAS (
  ID_FORMACION NUMBER(10),
  ID_HOJAVIDA NUMBER(10),
  NOM_INSTITUCION CHAR(50),
  TITULO CHAR(50),
  FECHA_INICIO DATE,
  FECHA_FINAL DATE,
  CONSTRAINT PK_FORMACION PRIMARY KEY (ID_FORMACION),
  CONSTRAINT FK_FORMACION_HOJA_VIDA FOREIGN KEY (ID_HOJAVIDA) REFERENCES HOJAS_DE_VIDA(ID_HOJA_VIDA)
);

-------------------------------
CREATE TABLE EXP_LABORALES (
  ID_EXP NUMBER(10),
  ID_HOJAVIDA NUMBER(10),
  NOM_EMPRESAS CHAR(50),
  TIEMPO_INICIO DATE,
  TIEMPO_FINAL DATE,
  CARGO CHAR(30),
  DESCRIPCION VARCHAR2(1000),
  CONSTRAINT PK_EXP_LABORALES PRIMARY KEY (ID_EXP),
  CONSTRAINT FK_EXP_LABORALES_HOJA_VIDA FOREIGN KEY (ID_HOJAVIDA) REFERENCES HOJAS_DE_VIDA(ID_HOJA_VIDA)
);

-------------------------------

CREATE TABLE DOC_ADMIN(
  ID_DOCS_ADMIN NUMBER(10),
  CONSTRAINT PK_DOC_ADMIN PRIMARY KEY (ID_DOCS_ADMIN)
);

