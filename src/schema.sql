DROP TABLE if EXISTS users;
 CREATE TABLE users (
 userid INTEGER PRIMARY KEY autoincrement,
 username text not null,
 password text not null);
