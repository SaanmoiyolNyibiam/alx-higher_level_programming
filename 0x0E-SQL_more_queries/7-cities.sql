-- This is an SQL script that creates the database hbtn_0d_usa
-- and the table cities (in the database hbtn_0d_usa)
-- on your MySQL server.

-- set up the database and switch to it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- set up table in the database
DROP TABLE IF EXISTS cities;

CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
    );

