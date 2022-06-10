USE mydb;

# *** Tipos de Produtos
select * from tipos_produtos;

insert into tipos_produtos (tipo) Value ('Produtos Acabados');
insert into tipos_produtos (tipo) Value ('Materia Prima');
insert into tipos_produtos (tipo) Value ('Imobilizado');
insert into tipos_produtos (tipo) Value ('Servicos');
insert into tipos_produtos (tipo) Value ('Material Auxiliar');
insert into tipos_produtos (tipo) Value ('Inativos');

# *** Fabricantes
select * from fabricantes_fornecedores;

INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Melitta');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Pimpinela');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('3 Corações');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Fazenda Colorado');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Melkstad Agropecuária Ltda');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Sekita Agronegócios');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('Guarani');
INSERT INTO fabricantes_fornecedores (Nome) VALUES ('prestoalimentos');

# *** Clientes
select * from clientes;

INSERT INTO clientes (Nome, Telefone, Endereco, Cep, Localidade, cpf)
VALUES ('Winona Ryder', 'Rua 01', '41912123030', '81000000', 'Curitiba', '234.235.236-37');

INSERT INTO clientes (Nome, Telefone, Endereco, Cep, Localidade, cpf)
VALUES ('David Harbour', 'Rua Tramontina', '41912345678', '81000000', 'Curitiba', '345.235.652-38');

INSERT INTO clientes (Nome, Telefone, Endereco, Cep, Localidade, cpf)
VALUES ('Millie Bobby Brown', 'Rua Intercambeavel', '41992345678', '81000000', 'Curitiba', '455.245.652-48');

INSERT INTO clientes (Nome, Telefone, Endereco, Cep, Localidade, cpf)
VALUES ('Finn Wolfhard', 'Rua Pointer', '41986345678', '81000000', 'Curitiba', '564.354.762-38');

# *** Produtos
SELECT * FROM produtos;

INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Cappuccino', 'Bebida', 'Cafe expresso e Leite Vaporizado', '7.0', '1', '1');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Frappuccino', 'Bebida', 'Leite Batido, Cafe, Chocolate em Po, Calda de Chocolate, Acucar, Chocolate Picado', '15.0', '1', '4');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Macchiato', 'Bebida', 'Cafe, Leite Vaporizado, Essencia de Baunilha', '10.0', '1', '4');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Cafe latte', 'Bebida', 'Cafe expresso com uma quantidade generosa de leite', '10.0', '1', '5');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Mocha', 'Bebida', 'Cafe espresso, leite vaporizado, chocolate e chantilly', '10.0', '1', '1');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('NAKED', 'Bebida', 'Cafe espresso', '5.0', '1', '1');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Brasileirinho', 'Bebida', 'Cappuccino Brasileiro', '7.0', '1', '1');
---
INSERT INTO produtos (Produto, Designacao, Composicao, Valor, Id_Tipo_Produto, Id_Fabricantes_Fornecedores)
VALUES ('Coxinha de Frango', 'Comida', 'Frango, Batata', '5.0', '1', '8');

# *** Compras
SELECT * FROM compras;

INSERT INTO compras (Id_Cliente, Data) Values (1, '2022-06-10');
INSERT INTO compras (Id_Cliente, Data) Values (2, '2022-06-10');
INSERT INTO compras (Id_Cliente, Data) Values (1, '2022-06-05');
INSERT INTO compras (Id_Cliente, Data) Values (1, '2022-06-05');
INSERT INTO compras (Id_Cliente, Data) Values (3, '2022-06-07');
INSERT INTO compras (Id_Cliente, Data) Values (4, '2022-06-07');

# *** Produtos Compras
SELECT * FROM produtos_compras;

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (1, 1, 2);

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (1, 2, 2);

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (2, 3, 1);

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (3, 4, 1);

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (3, 8, 1);

insert into produtos_compras (Id_compra, Id_Produto, Quantidade)
values (4, 8, 1);

# *** Funcionario
SELECT * FROM funcionarios;

Insert into funcionarios (Nome, Cracha)
values ('Jambiscladyson Duarticon', 1);

Insert into funcionarios (Nome, Cracha)
values ('Grandispjonison Clebis', 2);

# *** Nota Fiscal
SELECT * FROM nota_fiscal;

insert into nota_fiscal (Id_Produtos_Compras, Id_Funcionario, Valor_Total)
values (1, 2, 20.0);
