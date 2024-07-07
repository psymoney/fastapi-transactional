-- Create a new schema
CREATE DATABASE IF NOT EXISTS test;

-- Create a new user and grant privileges
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON test.* TO 'username'@'%';
FLUSH PRIVILEGES;
