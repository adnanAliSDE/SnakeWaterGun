CREATE DATABASE swg;
USE swg;

-- users
CREATE TABLE users(
id INT PRIMARY KEY auto_increment,
username VARCHAR(30) NOT NULL UNIQUE,
full_name VARCHAR(30),
score INT,
password VARCHAR(255)
);

-- games 
CREATE TABLE games(
id INT PRIMARY KEY AUTO_INCREMENT,
player_1 INT,
player_2 INT,
played_at timestamp DEFAULT NOW(),
FOREIGN KEY (player_1) references users(id),
FOREIGN KEY (player_2) references users(id)
);

