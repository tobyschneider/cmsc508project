from flask import render_template, redirect, url_for, request, flash, session
from app import app
from app.forms import LoginForm, ApplyForm, AnimalForm, WorkerForm
from passlib.hash import sha256_crypt
from dbconnect import connection
from functools import wraps
import gc
import datetime

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash("You need to log in first")
      return redirect(url_for('employeeLogin'))

  return wrap

@app.route('/')
@app.route('/index')
def index():
  c, conn = connection()
  c.execute("SELECT * FROM animal WHERE availID = 2")
  animals = c.fetchall()
  c.close()
  conn.close()
  return render_template('index.html', animals=animals) 

@app.route('/login', methods=['GET', 'POST'])
def employeeLogin():
  try:
    c, conn = connection()
    form = LoginForm(request.form)
    if request.method == "POST":
        data = c.execute("SELECT p.* FROM person p INNER JOIN employee e WHERE p.pid=e.empID AND username = (%s)", [request.form['username']]) # get usernames of all employees that match username form input
        data = c.fetchone()
        hashpw = data[8] # get hashed password from returned tuple

        if sha256_crypt.verify(request.form['password'], hashpw):
          session['logged_in'] = True #set logged_in session variable, necessary to access pages restricted by login_required decorator
          flash("Employee logged in successfully")
          return redirect(url_for('dashboard'))

        else:
          flash("Invalid credentials, try again.")
    c.close()
    conn.close()
    gc.collect()
    return render_template('login.html', form=form)

  except:
    flash("Invalid credentials, try again.")
    return render_template('login.html', form=form)    

@app.route('/apply', methods=['GET','POST'])
def apply():
  try:
    form = ApplyForm(request.form)

    if request.method == "POST" and form.validate(): #if form has valid inputs
      personName = form.name.data
      animalName = form.animalName.data
      address = form.address.data
      zip = form.zip.data
      pdob = form.dob.data
      email = form.email.data
      username = form.username.data
      password = sha256_crypt.encrypt((str(form.password.data)))
      c, conn = connection()

      x = c.execute("SELECT * FROM person WHERE username = (%s)", [(username)])
      # check if username is unique
      if int(x) > 0:
        flash("Username is already taken")
        return render_template('apply.html', form=form)

      else:
        date = datetime.date.today().strftime("%Y-%m-%d")
        c.execute("INSERT INTO person (pid, bid, personName, address, zip, pdob, email, username, password) VALUES (NULL, 2, %s, %s, %s, %s, %s, %s, %s)", (personName, address, zip, pdob, email, username, password)) #insert into person
        c.execute("INSERT INTO application (appID, pid, aID, appDate, appStatus) VALUES (NULL, (SELECT pid FROM person WHERE username = %s), (SELECT aID FROM animal WHERE animalName = %s), %s, 1)", (username, animalName, date)) #insert into application
        conn.commit()
        flash("Application submitted and user account registered!")
        c.close()
        conn.close()
        gc.collect()
        return redirect(url_for('index'))
        
    return render_template('apply.html', form=form)
  except Exception as e:
    return(str(e))

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/dashboard/addanimal', methods=['GET','POST'])
@login_required
def addAnimal():
    form = AnimalForm(request.form)
    if request.method == "POST" and form.validate(): #if form has valid inputs
        aType = form.aType.data
        animalName = form.animalName.data
        adob = form.adob.data
        asize = form.asize.data
        breed = form.breed.data
        availID = form.availID.data
        behaviorID = form.behaviorID.data
        poundID = form.poundID.data
        dateIn = form.dateIn.data
        c, conn = connection()
   
        c.execute("INSERT INTO animal (aID, aType, animalName, adob, size, breed, availID, behaviorID, poundID, dateIn) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (aType, animalName, adob, asize, breed, availID, behaviorID, poundID, dateIn)) #insert into person
      
        conn.commit()
        flash("Animal added!")
        c.close()
        conn.close()
        gc.collect()
        return redirect(url_for('addAnimal'))

    else:  
      return render_template('addanimal.html', form=form)



@app.route('/dashboard/addworker', methods=['GET','POST'])
@login_required
def addWorker(): 
  form = WorkerForm(request.form)
  if request.method == "POST" and form.validate(): #if form has valid inputs
      eType = form.eType.data
      personName = form.name.data
      address = form.address.data
      zip = form.zip.data
      pdob = form.dob.data
      email = form.email.data
      username = form.username.data
      password = sha256_crypt.encrypt((str(form.password.data)))
      c, conn = connection()

      x = c.execute("SELECT * FROM person WHERE username = (%s)", [(username)])
      # check if username is unique
      if int(x) > 0:
        flash("Username is already taken, try another")
        return render_template('addworker.html', form=form)
        
      else:  
        date = datetime.date.today().strftime("%Y-%m-%d")
        c.execute("INSERT INTO person (pid, bid, personName, address, zip, pdob, email, username, password) VALUES (NULL, 2, %s, %s, %s, %s, %s, %s, %s)", (personName, address, zip, pdob, email, username, password)) #insert into person
        c.execute("INSERT INTO worker (workerID, startDate, scheduleID) VALUES ((SELECT pid FROM person WHERE username = %s), %s, NULL)", (username, date))
        
        if (eType == "employee"):
          c.execute("INSERT INTO employee(empID) VALUES((SELECT pid FROM person WHERE username = %s))", (username))
          conn.commit()
          flash("Employee added!")
          c.close()
          conn.close()
          gc.collect()
          return render_template('addworker.html', form=form)
        else:
          c.execute("INSERT INTO volunteer(volID) VALUES((SELECT pid FROM person WHERE username = %s))", (username))
          conn.commit()
          flash("Volunteer added!")
          c.close()
          conn.close()
          gc.collect()
          return render_template('addworker.html', form=form)
         
  else:  
      return render_template('addworker.html', form=form)
@app.route('/dashboard/viewapps')
@login_required
def viewApps():
  c, conn = connection()
  c.execute("SELECT * FROM application")
  apps = c.fetchall()
  c.close()
  conn.close()
  return render_template('viewapps.html', apps=apps) 
# @app.route('/dashboard/schedule')
# def viewSchedule():

@app.route('/logout')
@login_required
def logout():
  session.clear()
  flash("Logged out successfully.")
  gc.collect()
  return redirect(url_for('index'))