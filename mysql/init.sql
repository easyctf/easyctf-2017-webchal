create database injection1;
create user 'injection1'@'%' identified by 'injection1';

use injection1;
drop table if exists users;
create table users (
    id int primary key auto_increment,
    username varchar(256),
    password varchar(256)
);

insert into users (username, password) values ("admin", "uSZjrv9fCfuzOWW6Uvv75mPQB7WsYjEYCFhewK8HvXup8zNItJ");
grant select on users to 'injection1'@'%' identified by 'injection1';


-- start injection 2

create database injection2;
create user 'injection2'@'%' identified by 'injection2';

use injection2;
drop table if exists users;
create table users (
    id int primary key auto_increment,
    username varchar(256),
    password varchar(256),
    power_level int
);

grant select on users to 'injection2'@'%' identified by 'injection2';


-- end injection 2


create database blogbox;
create user 'blogbox'@'%' identified by 'blogbox';
use blogbox;
drop table if exists posts;
grant select on blogbox . * to 'blogbox'@'%' identified by 'blogbox';
grant create on blogbox . * to 'blogbox'@'%' identified by 'blogbox';
grant drop on blogbox . * to 'blogbox'@'%' identified by 'blogbox';
grant insert on blogbox . * to 'blogbox'@'%' identified by 'blogbox';
