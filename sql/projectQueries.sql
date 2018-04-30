-- Create view that joins the volunteers with the workers with the people to get volunteer data  
DROP VIEW IF EXISTS volunteerInfo;
CREATE VIEW volunteerInfo AS (select * from volunteer inner join worker on volID=workerID inner join person on workerID=pid);

DROP VIEW IF EXISTS employeeInfo;
CREATE VIEW employeeInfo AS (select * from employee inner join worker on empID=workerID inner join person on workerID=pid);

DROP VIEW IF EXISTS fosterInfo;
CREATE VIEW fosterInfo AS (select * from foster inner join person on fostID=pid);

DROP VIEW IF EXISTS adopterInfo;
CREATE VIEW adopterInfo AS (select * from adopter inner join person on adoptID=pid);

-- Does Adopter/Foster A have a clean background check?
select personName, status from person natural join background where personName like 'Paige%';

-- What is the status of animal A?
select animalName, status from availability inner join animal on availability.availID=animal.availID;

-- List all animals of specific size/breed
select * from animal where breed like 'Mini%' and size='small';

-- List all available/fostered/adopted/deceased animals
select * from animal where availID = (select availID from availability where availability.status = 'unavailable');

-- The date that employee/volunteer started working
select personName, startDate from volunteerInfo;

-- What pound did an animal come from?
select animalName, poundName from animal inner join pound on animal.poundID=pound.poundID;

select animalName, poundName from animal inner join pound on animal.poundID=pound.poundID
where animalName like 'Poppie%';

-- Show all recently adopted/fostered animals from a certain period of time

-- Show animal breed/size preference of individual A --PROBELM IS GOING TO BE KNWOING IF SOMEONE IS AN ADOPTER OR FOSTER
select fostID, breedPref from foster;

-- How many applications has individual A submitted?
select personName, count(pid) from application natural join person;

-- How many applications have been received from a certain period of time? -- DONT KNOW THIS ONE --
select * from application where appDate = (MONTH('April') and YEAR('2018'));

-- What days are volunteer/employee A scheduled for?

-- How many (Which) background checks are processing/accepted/denied?
select status, count(status) from background
group by status;

-- Show all animals of personality trait A (ex. Friendly, needs outdoor space, good with children, etc.)
select * from animal where behaviorID = (select behaviorID from behavior where color ='red');

-- List all animals that are unavailable for adoption
select * from animal where availID = (select availID from availability where status='unavailable');

-- List all fosters/volunteers/adopters who live in a specific area
select * from person
where zip=23114;

-- How many applications does animal A have pending?
select animalName, count(pid) from application natural join animal
where appStatus = 'pending';

-- List all puppies/kittens 
select animalName from animal
where (YEAR(CURDATE())-adob < 3);

-- List all adult animals 
select animalName from animal
where (YEAR(CURDATE())-adob > 3);

-- How many volunteers are scheduled for a certain day?
select personName from volunteer natural join worker natural join workerschedule natural join person
where monday = false;


-- DELIMITER $$
-- DROP TRIGGER IF EXISTS applicationDates;
-- CREATE TRIGGER applicationDates AFTER UPDATE ON application
-- FOR EACH ROW
-- BEGIN
-- if appStatus = 'accepted' 
-- then set appDate = now();
-- end if;
-- END$$

-- DELIMITER ;
