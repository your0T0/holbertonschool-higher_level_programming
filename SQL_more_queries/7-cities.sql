-- Creates table cities in hbtn_0d_usa
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT NOT NULL AUTO_INCREMENT,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (id),
  CONSTRAINT fk_cities_state FOREIGN KEY (state_id) REFERENCES states(id)
);
