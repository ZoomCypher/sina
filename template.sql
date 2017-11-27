create database sina_topic character set utf8;


CREATE TABLE child_abuse
(
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
comment VARCHAR(300) NOT NULL
);

mysqldump -u root -p -d sina_topic child_abuse > child_abuse.sql

 select * into outfile 'C:/Users/lxd02/Desktop/sina/child.txt' from child_abuse;