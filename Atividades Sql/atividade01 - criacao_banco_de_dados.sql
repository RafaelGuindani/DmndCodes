# Data Definition Language

CREATE DATABASE secao04;
USE secao04;
CREATE TABLE tipos_produtos(
	codigo INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(55) NOT NULL,
    PRIMARY KEY(codigo)
);
CREATE TABLE produtos(
	codigo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(30) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    codigo_tipo INT NOT NULL,
    FOREIGN KEY (codigo_tipo) REFERENCES tipos_produtos(codigo)
);

#Data Manipulation Language

INSERT INTO tipos_produtos (descricao) VALUES ('Computadores');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressoras');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Notebook', '2200', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impressora Jato de Tinta', '350', 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impressora Laser', '500', 2);

# DQL
# Data Querry Language

# Comandos de seleção iguais:

SELECT * FROM tipos_produtos;
SELECT codigo, descricao FROM tipos_produtos;

# Não imposta a ordem da solicitação, será executado.
SELECT descricao, codigo FROM tipos_produtos;

SELECT codigo, descricao, preco, codigo_tipo FROM produtos;

# ALIAS - APELIDO
SELECT p.codigo AS cod, p.descricao AS descri, p.preco as pre, p.codigo_tipo as ctp FROM produtos AS p;
