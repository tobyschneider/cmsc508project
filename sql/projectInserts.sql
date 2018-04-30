INSERT INTO workerschedule VALUES(NULL, false, true, false, true, true, true, false);

INSERT INTO animal VALUES (NULL, 'dog','Poppie','2001', 'small','Miniature Pincher',3,3,1,2008);
INSERT INTO animal VALUES(NULL, 'dog', 'Bailey','2010', 'large', 'Golden Doodle', 1,2,4, 2013);
INSERT INTO animal VALUES(NULL, 'dog', 'Daisy','2017', 'medium', 'Beagle',2,1,3,2007);


INSERT INTO person VALUES(NULL, 1,'Paige Fuller', '13806 Bach Court Midlothian VA', 23114,'1997-06-17', 'pj.fuller@hotmail.com');
INSERT INTO person VALUES(NULL, 2,'Tobias Schneider', '111 Butts Lane Richmond VA', 23221,'1997-03-23', 'tobyschneider@vcu.edu');

INSERT INTO worker VALUES((SELECT pid from person where personName = 'Paige Fuller'), '2018-04-08', 1);
INSERT into volunteer VALUES((SELECT workerID from worker natural join person where personName = 'Tobias Schneider'));
INSERT into foster VALUES((SELECT workerID from worker natural join person where personName = 'Paige Fuller'), 'small', 'Miniature Pincher', 'dog');

INSERT into application VALUES(NULL, (SELECT pID from worker natural join person where personName = 'Paige Fuller'),(SELECT aid from animal where animalName='Poppie'), '2018-04-08','accepted');
INSERT into application VALUES(NULL, (SELECT pID from worker natural join person where personName = 'Tobias Schneider'),(SELECT aid from animal where animalName='Poppie'), '2018-04-08','rejected');

INSERT into application VALUES(NULL, (SELECT pID from worker natural join person where personName = 'Paige Fuller'),(SELECT aid from animal where animalName='Daisy'), '2018-04-08','pending');
INSERT into application VALUES(NULL, (SELECT pID from worker natural join person where personName = 'Tobias Schneider'),(SELECT aid from animal where animalName='Daisy'), '2018-04-08','pending');

