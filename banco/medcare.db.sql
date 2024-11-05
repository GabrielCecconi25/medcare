BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS atendimento (id INTEGER PRIMARY KEY AUTOINCREMENT,status TEXT,tipo TEXT,data DATE);
CREATE TABLE IF NOT EXISTS consultorio(id INTEGER	PRIMARY KEY AUTOINCREMENT, numero INTEGER, ocupacao	TEXT);
CREATE TABLE IF NOT EXISTS convenio (id INTEGER PRIMARY KEY AUTOINCREMENT, empresa TEXT, plano TEXT, numero INTEGER);
CREATE TABLE IF NOT EXISTS medico (id INTEGER PRIMARY KEY AUTOINCREMENT, crm INTEGER, nome TEXT, especialidade TEXT);
CREATE TABLE IF NOT EXISTS "paciente" (
	"id"	INTEGER,
	"cpf"	INTEGER UNIQUE,
	"nome"	TEXT,
	"rg"	TEXT,
	"idade"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS senha (id INTEGER PRIMARY KEY AUTOINCREMENT, status TEXT, horario datetime, numero	INTEGER);
INSERT INTO "consultorio" ("id","numero","ocupacao") VALUES (1,1,NULL),
 (2,2,NULL),
 (3,3,NULL),
 (4,4,NULL),
 (5,5,NULL);
INSERT INTO "medico" ("id","crm","nome","especialidade") VALUES (1,248376,'Breno Sérgio Thomas Pereira','Clínico Geral'),
 (2,557396,'Anderson Diego Cavalcanti','Ortopedia'),
 (3,690399,'Caleb Kaique Silveira','Ortopedia'),
 (4,815022,'Nina Antônia Moreira','Clínico Geral'),
 (5,930091,'Elaine Cláudia Figueiredo','Pediatria');
COMMIT;
