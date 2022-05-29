# Inserindo dados - DML
# *** Tipos de Produtos
USE db_cafeteria;
INSERT INTO tipos_produtos (descricao) VALUES ('Cappuccino');
INSERT INTO tipos_produtos (descricao) VALUES ('Frappuccino');
INSERT INTO tipos_produtos (descricao) VALUES ('Macchiato');
INSERT INTO tipos_produtos (descricao) VALUES ('Café latte');
INSERT INTO tipos_produtos (descricao) VALUES ('Mocha');
INSERT INTO tipos_produtos (descricao) VALUES ('NAKED');
INSERT INTO tipos_produtos (descricao) VALUES ('Brasileirinho');

# ** Adicionar coluna tabela tipos_produtos
alter table tipos_produtos add column Quantidade varchar(55);
# -- Visualizar a planilha
SELECT * FROM tipos_produtos;

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
