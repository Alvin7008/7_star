use  seven_stars;
create table vehicletype (id int AUTO_INCREMENT,  vehtype varchar(255) not null, flag int, primary key(id));
select * from vehicletype;
alter table vehicletype alter id  set Default 1001;
show databases;
select * from users;
select max(id) as id from users;
truncate table users;
alter table users change id id INT(40) AUTO_INCREMENT;
