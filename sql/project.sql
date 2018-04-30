
-- 	Database Table Creation

--  First drop any existing tables. Any errors are ignored.
SET FOREIGN_KEY_CHECKS = 0;
drop table if exists person;
drop table if exists  worker;
drop table if exists  employee;
drop table if exists  volunteer;
drop table if exists  foster;
drop table if exists  adopter;
drop table if exists  background;
drop table if exists  workerSchedule;
drop table if exists  application;
drop table if exists  animal;
drop table if exists cat;
drop table if exists  dog;
drop table if exists  pound;
drop table if exists  behavior;
drop table if exists availability;
SET FOREIGN_KEY_CHECKS = 1;

-- Now, add each table.

drop table if exists background;
create table background(
	bid int NOT NULL auto_increment primary key,
    status ENUM('pending','clear','rejected')
    );

drop table if exists person;
create table person(
	pid int NOT NULL auto_increment primary key,
    bid int,
    personName varchar(30),
    address varchar(50),
    zip int,
    pdob date,
    email varchar(30),
    username varchar(30),
    password varchar(50),
    foreign key(bid) references background(bid)
	);
    
drop table if exists workerSchedule;
create table workerSchedule(
	scheduleID int NOT NULL auto_increment primary key,
	monday bool,
	tuesday bool,
	wednesday bool,
	thursday bool,
    friday bool,
    saturday bool,
    sunday bool
	);
 

drop table if exists worker;
create table worker(
	workerID int,
	startDate date CHECK (YEAR(date) <= YEAR(CURDATE())),
    scheduleID int,
    foreign key(scheduleID) references workerSchedule(scheduleID),
    foreign key(workerID) references person(pid)
	);
    
    
drop table if exists employee;
create table employee(
	empID int,
	foreign key(empID) references worker(workerID)
	);

drop table if exists volunteer;
create table volunteer(
	volID int,
	foreign key(volID) references worker(workerID)
	);

drop table if exists foster;
create table foster(
	fostID int,
	sizePref ENUM('small', 'medium', 'large'),
	breedPref varchar(50),
	animalPref ENUM('cat','dog'),
    foreign key(fostID) references person(pid)
	);
    
drop table if exists adopter;
create table adopter(
	adoptID int,
	sizePref ENUM('small', 'medium', 'large'),
	breedPref varchar(50),
	animalPref ENUM('cat','dog'),
    foreign key(adoptID) references person(pid)
	);
    
drop table if exists availability;
create table availability(
	availID int NOT NULL auto_increment primary key,
    status ENUM('available','unavailable','fostered','adopted','deceased')
    );

drop table if exists pound;
create table pound(
	poundID int NOT NULL auto_increment primary key,
    poundName varchar(100)
    );
    
drop table if exists behavior;
create table behavior(
	behaviorID int NOT NULL auto_increment primary key,
    color ENUM('pink','yellow','red','blue')
    );

drop table if exists animal;
create table animal(
	aID int NOT NULL auto_increment primary key,
    aType ENUM('dog','cat'),
    animalName varchar(20),
    adob YEAR, CHECK (adob <= YEAR(CURRDATE())),
    size ENUM('small','medium','large'),
    breed varchar(20),
    availID int,
    behaviorID int,
    poundID int,
    dateIn YEAR, CHECK (dateIn <= YEAR(CURRDATE())), CHECK(dateIn >= adob),
    foreign key(availID) references availability(availID),
	foreign key(behaviorID) references behavior(behaviorID),
	foreign key(poundID) references pound(poundID)
    );

drop table if exists application;
create table application(
	appID int NOT NULL auto_increment primary key,
    pid int,
    aID int,
    appDate date, CHECK (YEAR(date) <= YEAR(CURDATE())),
    appStatus ENUM('pending','accepted','rejected'),
    foreign key(pid) references person(pid),
    foreign key(aID) references animal(aID)
    );
    

   
   
   

alter table person
	add constraint
	 foreign key(bid) references background(bid);

alter table worker
	add constraint
	foreign key(scheduleID) references workerSchedule(scheduleID);
alter table worker
	add constraint
    foreign key(workerID) references person(pid);

alter table employee
	add constraint
	foreign key(empID) references worker(workerID);
    
alter table foster
	add constraint
	 foreign key(fostID) references person(pid);

alter table adopter
	add constraint
	foreign key(adoptID) references person(pid);
    
alter table application
	add constraint
	foreign key(pID) references person(pid);
alter table application
	add constraint
	foreign key(aID) references animal(aID);
    
alter table animal
	add constraint
	foreign key(availID) references availability(availID);
alter table animal
	add constraint    
    foreign key(behaviorID) references behavior(behaviorID);
alter table animal
	add constraint
	foreign key(poundID) references pound(poundID);
    


    

