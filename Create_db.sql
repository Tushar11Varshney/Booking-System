create database corona_db;
use corona_db;
CREATE TABLE USER(
	user_id INT primary key,
    name varchar(50) not null
);

SELECT * FROM corona_db.user;
describe corona_db.user;

-- make auto increment id
ALTER TABLE USER
MODIFY COLUMN user_id INT AUTO_INCREMENT;

delete from user;

-- Truncate the user table to remove all data and reset the auto-increment primary key. Cannot truncate a table referenced in a foreign key.
-- TRUNCATE TABLE user; 
ALTER TABLE user AUTO_INCREMENT = 1;

INSERT INTO USER (name) VALUES ('Aarav');
INSERT INTO USER (name) VALUES ('Aadrika');
INSERT INTO USER (name) VALUES ('Aanya');
INSERT INTO USER (name) VALUES ('Abhinav');
INSERT INTO USER (name) VALUES ('Advait');
INSERT INTO USER (name) VALUES ('Alisha');
INSERT INTO USER (name) VALUES ('Amaira');
INSERT INTO USER (name) VALUES ('Ananya');
INSERT INTO USER (name) VALUES ('Arjun');
INSERT INTO USER (name) VALUES ('Aryan');
INSERT INTO USER (name) VALUES ('Atharva');
INSERT INTO USER (name) VALUES ('Avani');
INSERT INTO USER (name) VALUES ('Ayush');
INSERT INTO USER (name) VALUES ('Chahat');
INSERT INTO USER (name) VALUES ('Dhruv');
INSERT INTO USER (name) VALUES ('Eesha');
INSERT INTO USER (name) VALUES ('Evaan');
INSERT INTO USER (name) VALUES ('Gauri');
INSERT INTO USER (name) VALUES ('Harshita');
INSERT INTO USER (name) VALUES ('Ishan');
INSERT INTO USER (name) VALUES ('Ishani');
INSERT INTO USER (name) VALUES ('Jai');
INSERT INTO USER (name) VALUES ('Kabir');
INSERT INTO USER (name) VALUES ('Kavya');
INSERT INTO USER (name) VALUES ('Krish');
INSERT INTO USER (name) VALUES ('Laksh');
INSERT INTO USER (name) VALUES ('Mira');
INSERT INTO USER (name) VALUES ('Mohit');
INSERT INTO USER (name) VALUES ('Navya');
INSERT INTO USER (name) VALUES ('Neha');
INSERT INTO USER (name) VALUES ('Ojas');
INSERT INTO USER (name) VALUES ('Parth');
INSERT INTO USER (name) VALUES ('Prisha');
INSERT INTO USER (name) VALUES ('Rachit');
INSERT INTO USER (name) VALUES ('Rahul');
INSERT INTO USER (name) VALUES ('Ria');
INSERT INTO USER (name) VALUES ('Rohan');
INSERT INTO USER (name) VALUES ('Ruhi');
INSERT INTO USER (name) VALUES ('Saisha');
INSERT INTO USER (name) VALUES ('Samar');
INSERT INTO USER (name) VALUES ('Sanvi');
INSERT INTO USER (name) VALUES ('Sarthak');
INSERT INTO USER (name) VALUES ('Sia');
INSERT INTO USER (name) VALUES ('Siddharth');
INSERT INTO USER (name) VALUES ('Simran');
INSERT INTO USER (name) VALUES ('Tanvi');
INSERT INTO USER (name) VALUES ('Trisha');
INSERT INTO USER (name) VALUES ('Utkarsh');
INSERT INTO USER (name) VALUES ('Vaibhav');
INSERT INTO USER (name) VALUES ('Vanshika');
INSERT INTO USER (name) VALUES ('Vedant');
INSERT INTO USER (name) VALUES ('Vidhi');
INSERT INTO USER (name) VALUES ('Vihaan');
INSERT INTO USER (name) VALUES ('Yash');
INSERT INTO USER (name) VALUES ('Yuvraj');
INSERT INTO USER (name) VALUES ('Zara');
INSERT INTO USER (name) VALUES ('Aahana');
INSERT INTO USER (name) VALUES ('Aaditya');
INSERT INTO USER (name) VALUES ('Aanya');
INSERT INTO USER (name) VALUES ('Abhay');
INSERT INTO USER (name) VALUES ('Advika');
INSERT INTO USER (name) VALUES ('Agastya');
INSERT INTO USER (name) VALUES ('Akanksha');
INSERT INTO USER (name) VALUES ('Alok');
INSERT INTO USER (name) VALUES ('Aarohi');
INSERT INTO USER (name) VALUES ('Amit');
INSERT INTO USER (name) VALUES ('Amisha');
INSERT INTO USER (name) VALUES ('Ankit');
INSERT INTO USER (name) VALUES ('Anvi');
INSERT INTO USER (name) VALUES ('Arnav');
INSERT INTO USER (name) VALUES ('Arya');
INSERT INTO USER (name) VALUES ('Ashish');
INSERT INTO USER (name) VALUES ('Avishi');
INSERT INTO USER (name) VALUES ('Bhavesh');
INSERT INTO USER (name) VALUES ('Bhavya');
INSERT INTO USER (name) VALUES ('Chaitanya');
INSERT INTO USER (name) VALUES ('Deeksha');
INSERT INTO USER (name) VALUES ('Dev');
INSERT INTO USER (name) VALUES ('Disha');
INSERT INTO USER (name) VALUES ('Divya');
INSERT INTO USER (name) VALUES ('Eshaan');
INSERT INTO USER (name) VALUES ('Fatima');
INSERT INTO USER (name) VALUES ('Garima');
INSERT INTO USER (name) VALUES ('Gautam');
INSERT INTO USER (name) VALUES ('Gayatri');
INSERT INTO USER (name) VALUES ('Hansika');
INSERT INTO USER (name) VALUES ('Hridyansh');
INSERT INTO USER (name) VALUES ('Ira');
INSERT INTO USER (name) VALUES ('Ishaan');
INSERT INTO USER (name) VALUES ('Ishika');
INSERT INTO USER (name) VALUES ('Jhanvi');
INSERT INTO USER (name) VALUES ('Jignesh');
INSERT INTO USER (name) VALUES ('Jyoti');
INSERT INTO USER (name) VALUES ('Kabir');
INSERT INTO USER (name) VALUES ('Kanishka');
INSERT INTO USER (name) VALUES ('Kartik');
INSERT INTO USER (name) VALUES ('Kritika');
INSERT INTO USER (name) VALUES ('Kush');
INSERT INTO USER (name) VALUES ('Kyra');
INSERT INTO USER (name) VALUES ('Lakshay');
INSERT INTO USER (name) VALUES ('Mahi');
INSERT INTO USER (name) VALUES ('Manav');
INSERT INTO USER (name) VALUES ('Manvi');
INSERT INTO USER (name) VALUES ('Mayank');
INSERT INTO USER (name) VALUES ('Mehak');
INSERT INTO USER (name) VALUES ('Mohini');
INSERT INTO USER (name) VALUES ('Mukul');
INSERT INTO USER (name) VALUES ('Naina');
INSERT INTO USER (name) VALUES ('Naksh');
INSERT INTO USER (name) VALUES ('Navya');
INSERT INTO USER (name) VALUES ('Nehal');

INSERT INTO USER (name) VALUES
('John Smith'),
('Mary Johnson'),
('James Williams'),
('Patricia Jones'),
('Michael Brown'),
('Jennifer Davis'),
('David Miller'),
('Linda Wilson'),
('Christopher Martinez');

create table session (
	session_id int primary key,
    session_name varchar(50) not null
);
insert into session (session_id, session_name) values (1, "COVID-VACCINE-1");
select * from session;

create table booking(
	seat_id int primary key,
    user_id int,
    session_id int,
    foreign key (user_id) references USER(user_id) on delete set null,
    foreign key (session_id) references session(session_id) on delete set null
);

-- make seat id varchar
-- Step 1: Drop the existing primary key constraint
ALTER TABLE booking
DROP PRIMARY KEY;
-- Step 2: Modify the data type of the primary key column to varchar
ALTER TABLE booking
MODIFY COLUMN seat_id VARCHAR(50);
-- Step 3: Create a new primary key constraint using the updated column
ALTER TABLE booking
ADD PRIMARY KEY (seat_id);


-- make id as primary key
ALTER TABLE booking
DROP PRIMARY KEY;
ALTER TABLE booking
ADD COLUMN id INTEGER AUTO_INCREMENT PRIMARY KEY;

-- insert into booking (seat_id, session_id) values("1-A", 1); 

delete from booking;
alter table booking auto_increment=1; 

-- create entries
CREATE TEMPORARY TABLE letters (letter CHAR(1));
INSERT INTO letters (letter) VALUES ('A'),('B'),('C'),('D'),('E'),('F'),('G'),('H'),('I'),('J'),('K'),('L');
INSERT INTO booking (seat_id, user_id, session_id)
SELECT
  CONCAT(n.num, '-', l.letter) AS seat_id,
  NULL AS user_id,
  1 AS session_id
FROM (
  SELECT num FROM (SELECT 1 AS num UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
                   UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8
                   UNION ALL SELECT 9 UNION ALL SELECT 10) numbers 
) n
CROSS JOIN letters l;

select * from booking;
describe booking;
