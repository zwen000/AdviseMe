from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class StudentInfoForm(FlaskForm):
    EMPLID =IntegerField('EMPLID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    middlename =StringField('Middle Name', validators=[])
    credit_earned=IntegerField('Credit Earned', validators=[DataRequired()])
    credit_taken=IntegerField('Credit Taken', validators=[DataRequired()])
    graduating = BooleanField('Is Graduating?')
    submit = SubmitField('Update')

class FacultyInfoForm(FlaskForm):
    EMPLID =IntegerField('EMPLID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    middlename =StringField('Middle Name', validators=[])
    staff_role =StringField('Staff Role', validators=[DataRequired()])
    submit = SubmitField('Update')

class advisingNotesForm(FlaskForm):
    academic_comment = StringField('Academic Comment', validators=[DataRequired()])
    next_semester_comment = StringField('Next Semester Comment', validators=[DataRequired()])
    be_advised = BooleanField('Be advised?')
    submit = SubmitField('Approved')