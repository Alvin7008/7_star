use  seven_stars;
create table vehicletype (id int AUTO_INCREMENT,  vehtype varchar(255) not null, flag int, primary key(id));
select * from vehicletype;
alter table vehicletype alter id  set Default 1001;
show databases;
select * from users;
select max(id) as id from users;
truncate table users;
alter table users change id id INT(40) AUTO_INCREMENT;


CREATE TABLE `seven_stars`.`driver_details` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `emid` VARCHAR(255) NOT NULL,
  `licno` VARCHAR(255) NOT NULL,
  `emidvald` VARCHAR(255) NOT NULL,
  `licsdate` DATE NOT NULL,
  `licedate` DATE NOT NULL,
  `passportno` VARCHAR(255) NOT NULL,
  `validity` VARCHAR(255) NOT NULL,
  `sponsor` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));
