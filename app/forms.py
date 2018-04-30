from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class ApplyForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    animalName = StringField('Name of animal', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    zip = IntegerField('Zip Code', validators=[DataRequired()])
    dob = StringField('Date of birth (YYYY-MM-DD)', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50)])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField('Confirm password')
    submit = SubmitField('Apply')

class AnimalForm(FlaskForm):
    aType = SelectField(u'Animal type', choices=[('dog', 'dog'), ('cat', 'cat')], validators=[DataRequired()])
    animalName = StringField('Name of animal', validators=[DataRequired()])
    adob = StringField('Year of birth', validators=[DataRequired()])
    asize = SelectField(u'Animal size', choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    availID = IntegerField('Availability ID', validators=[DataRequired()])
    behaviorID = IntegerField('Behavior ID', validators=[DataRequired()])
    poundID = IntegerField('Pound ID', validators=[DataRequired()])
    dateIn = IntegerField('Date In (year)', validators=[DataRequired()])
    submit = SubmitField('Add animal')

class WorkerForm(FlaskForm):
    eType = SelectField(u'Worker type', choices=[('employee', 'employee'), ('volunteer', 'volunteer')], validators=[DataRequired()])
    name = StringField('Full name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    zip = IntegerField('Zip Code', validators=[DataRequired()])
    dob = StringField('Date of birth (YYYY-MM-DD)', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50)])
    startDate = StringField('Start date (YYYY-MM-DD)', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField('Confirm password')
    submit = SubmitField('Apply')