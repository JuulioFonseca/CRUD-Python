# CRUD-Python


SQL
CREATE TABLE `crudpython`.`fundosfii` (
  `idfundosfii` INT NOT NULL AUTO_INCREMENT,
  `name_fii` VARCHAR(45) NOT NULL,
  `pvp` DOUBLE NOT NULL,
  `cota` DOUBLE NOT NULL,
  `div_yield` DOUBLE NOT NULL,
  `valorizacao` DOUBLE NOT NULL,
  PRIMARY KEY (`idfundosfii`));