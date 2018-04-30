# CMSC508Project

# To Do
- [x] Employee login
- [x] Set up dashboard navigation
- [x] Add animals
- [ ] Create workers 
- [ ] Update background checks

## Installing dependencies 
- pip (python package manager)

- sudo pip install flask  (Main framework)

- sudo pip install flask-bootstrap  (Frontend framework)

- sudo pip install flask-mysqldb (MySQL interface)

- sudo pip install flask-wtf (Web form handler)

- sudo pip install passlib (password encryption)

# clone if necessary

- sudo git clone https://github.com/pjfuller/CMSC508Project/

## How to setup MySQL database
- Make sure mysqldb or mariadb is installed and running

- Edit dbconnect.py conn variable to match your mysql server credentials

- On MySQL command line, 
    - create database project;
    - use project;
    - source /path/to/CMSC508Project/sql/project.sql;          //creates tables                         
    - source /path/to/CMSC508Project/sql/SpecialInserts.sql 
    - source /path/to/CMSC508Project/sql/projectInserts.sql

## How to run the app
- Make sure all dependencies installed

- cd CMSC508Project/

- export FLASK_APP=project.py          //sets environment variable

- flask run
  - Will run on http://127.0.0.1:5000/  
