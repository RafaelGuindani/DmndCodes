-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_cafeteria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_cafeteria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_cafeteria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `db_cafeteria` ;

-- -----------------------------------------------------
-- Table `db_cafeteria`.`Tipos_Produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Tipos_Produtos` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Fabricantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Fabricantes` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `fabricante` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Fornecedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Fornecedores` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Produtos` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Produto` VARCHAR(45) NOT NULL,
  `Designacao` VARCHAR(45) NOT NULL,
  `Composicao` VARCHAR(45) NOT NULL,
  `Preco_Venda` VARCHAR(45) NOT NULL,
  `Id_Tipos_Produtos` INT NOT NULL,
  `Id_Fabricantes` INT NOT NULL,
  `Id_Fornecedores` INT NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Produtos_1_idx` (`Id_Tipos_Produtos` ASC) ,
  INDEX `fk_Produtos_2_idx` (`Id_Fabricantes` ASC) ,
  INDEX `fk_Produtos_3_idx` (`Id_Fornecedores` ASC) ,
  CONSTRAINT `fk_Produtos_1`
    FOREIGN KEY (`Id_Tipos_Produtos`)
    REFERENCES `db_cafeteria`.`Tipos_Produtos` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Produtos_2`
    FOREIGN KEY (`Id_Fabricantes`)
    REFERENCES `db_cafeteria`.`Fabricantes` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Produtos_3`
    FOREIGN KEY (`Id_Fornecedores`)
    REFERENCES `db_cafeteria`.`Fornecedores` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Clientes` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Endereco` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(20) NOT NULL,
  `Cep` VARCHAR(15) NOT NULL,
  `Localidade` VARCHAR(45) NOT NULL,
  `Cpf` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Compras` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Id_Cliente` INT NOT NULL,
  `Data` DATE NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Compras_1_idx` (`Id_Cliente` ASC) ,
  CONSTRAINT `fk_Compras_1`
    FOREIGN KEY (`Id_Cliente`)
    REFERENCES `db_cafeteria`.`Clientes` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Produtos_Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Produtos_Compras` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Id_Compra` INT NOT NULL,
  `Id_Produto` INT NOT NULL,
  `Quantidade` INT NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Produtos_Compras_1_idx` (`Id_Compra` ASC) ,
  INDEX `fl_Produtos_Compras_2_idx` (`Id_Produto` ASC) ,
  CONSTRAINT `fk_Produtos_Compras_1`
    FOREIGN KEY (`Id_Compra`)
    REFERENCES `db_cafeteria`.`Compras` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fl_Produtos_Compras_2`
    FOREIGN KEY (`Id_Produto`)
    REFERENCES `db_cafeteria`.`Produtos` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_cafeteria`.`Nota_Fiscal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_cafeteria`.`Nota_Fiscal` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Id_Produto_Compra` INT NOT NULL,
  `Codigo` INT NOT NULL,
  `Data` DATE NOT NULL,
  `Hora` TIME NOT NULL,
  `Valor_Pagamento` DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Nota_Fiscal_1_idx` (`Id_Produto_Compra` ASC) ,
  CONSTRAINT `fk_Nota_Fiscal_1`
    FOREIGN KEY (`Id_Produto_Compra`)
    REFERENCES `db_cafeteria`.`Produtos_Compras` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
