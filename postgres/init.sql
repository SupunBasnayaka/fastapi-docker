CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);

INSERT INTO users (name, age) VALUES
('Kamal', 25),
('Nimal', 22),
('Samal', 28);