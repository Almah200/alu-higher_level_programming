-- creates a database and atable with pry and foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL, 
PRIMARY KEY (id), 
FOREIGN KEY (state_id) REFERENCES states(id));
~
