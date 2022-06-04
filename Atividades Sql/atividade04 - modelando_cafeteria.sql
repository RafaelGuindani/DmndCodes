# Inserindo dados - DML
# *** Tipos de Produtos
USE db_cafeteria;

# -- Visualizar a planilha
SELECT * FROM tipos_produtos;

INSERT INTO tipos_produtos (descricao) VALUES ('Cappuccino');
INSERT INTO tipos_produtos (descricao) VALUES ('Frappuccino');
INSERT INTO tipos_produtos (descricao) VALUES ('Macchiato');
INSERT INTO tipos_produtos (descricao) VALUES ('Cafe latte');
INSERT INTO tipos_produtos (descricao) VALUES ('Mocha');
INSERT INTO tipos_produtos (descricao) VALUES ('NAKED');
INSERT INTO tipos_produtos (descricao) VALUES ('Brasileirinho');

# ** Adicionar coluna tabela tipos_produtos
alter table tipos_produtos add column Quantidade int(11) NOT NULL default;

# *** Tipos de Produtos
# *** Atualizando ID
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '1' WHERE (`Id` = '15');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '2' WHERE (`Id` = '16');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '3' WHERE (`Id` = '17');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '4' WHERE (`Id` = '18');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '5' WHERE (`Id` = '19');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '6' WHERE (`Id` = '20');
UPDATE `db_cafeteria`.`tipos_produtos` SET `Id` = '7' WHERE (`Id` = '21');

# *** Fabricantes
INSERT INTO fabricantes (fabricante) VALUES ('Melitta');
INSERT INTO fabricantes (fabricante) VALUES ('Pimpinela');
INSERT INTO fabricantes (fabricante) VALUES ('3 Corações');
INSERT INTO fabricantes (fabricante) VALUES ('3 Corações');
INSERT INTO fabricantes (fabricante) VALUES ('3 Corações');
INSERT INTO fabricantes (fabricante) VALUES ('Fazenda Colorado');
INSERT INTO fabricantes (fabricante) VALUES ('Melkstad Agropecuária Ltda');
INSERT INTO fabricantes (fabricante) VALUES ('Sekita Agronegócios');
INSERT INTO fabricantes (fabricante) VALUES ('Guarani');
