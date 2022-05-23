#DML
#Data Manipulation Language
USE secao04;

# -- iNSERT
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUE ('Notebook', '1200', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('IPAD Pro', '3200', 1);

# -- UPDATE
UPDATE produtos SET preco = 1800 WHERE codigo = 3;
UPDATE produtos SET preco = 250 WHERE codigo = 3;
UPDATE produtos SET preco = 1500 WHERE codigo = 5;

# -- DELETE
DELETE FROM produtos WHERE codigo = 5;

# -- Visualizar a planilha
SELECT * FROM produtos;
