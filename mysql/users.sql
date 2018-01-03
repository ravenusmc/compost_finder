-- This file will contain the code for the table layout. 

CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  address VARCHAR(240) NOT NULL,
  city VARCHAR(240) NOT NULL,
  state VARCHAR(2) NOT NUll,
  zipcode int NOT NUll,
  lat DECIMAL(9,5) NOT NUll,
  lng DECIMAL(9,5) NOT NULL,
  type VARCHAR(15) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);
