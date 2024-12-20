CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

SELECT * FROM friends;

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Heather Hathaway', '1985-10-23');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Raymond McGuire', '1987-06-03');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codeacademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'hhathaway10@hotmail.com'
WHERE id = 2;

UPDATE friends
SET email = 'ray.p.mcg@gmail.com'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends;
