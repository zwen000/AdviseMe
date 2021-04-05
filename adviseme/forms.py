from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import *
from adviseme.models import *
from datetime import date

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_EMPLID(self, EMPLID):              # checks for duplicate EMPLID's 
        user = User.query.filter_by(EMPLID = EMPLID.data).first()
        if user:
            raise ValidationError('That EMPLID is already in use!')
        
    def validate_email(self, email):                # checks for duplicate emails! 
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('The email is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class StudentInfoForm(FlaskForm):
    EMPLID = IntegerField('EMPLID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    picture = FileField('Update Profile Image', validators=[ FileAllowed(['jpg', 'png']) ])
    bio = TextAreaField('Student Bio (Optional)') # No validators here, since this is completely optional! 
    graduating = BooleanField('Is Graduating?')
    submit = SubmitField('Submit')

    def validate_EMPLID(self, EMPLID):              # checks for duplicate EMPLID's 
        user = User.query.filter_by(EMPLID = EMPLID.data).first()
        if user:
            raise ValidationError('That EMPLID is already in use!')


# Although you would think, that just hardcoding the grade values in the choices array would be good enough, this 
# needs to be query'd and connected to a grade table so a user can pick a grade choice ... 
 

class SubmitForm(FlaskForm):
    submit = SubmitField('Submit')
    
class CourseInfoForm(FlaskForm):
    grade = SelectField('grade: ', choices=[])
    submit = SubmitField('Submit')

class CourseCreationForm(FlaskForm):
    serial = StringField('Course Serial:', validators=[DataRequired()])
    name = StringField('Course Name:', validators=[DataRequired()])
    dept = StringField('Department:', validators=[DataRequired()])
    description = TextAreaField('Course Description: (Optional)')
    designation = StringField('Designation:', validators=[DataRequired()])
    credits = IntegerField('Course id:', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_Course_ID(self, id):              # checks for duplicate Course id's 
        course = Course.query.filter_by(id=id.data).first()
        if course:
            raise ValidationError('That Course ID is already in use!')


class ElectiveForm(FlaskForm):
    elective = SelectField('Elective: ', choices=[])
    grade = SelectField('grade: ', choices=[])
    submit = SubmitField('Submit')



class FacultyInfoForm(FlaskForm):
    EMPLID =IntegerField('EMPLID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    picture = FileField('Update Profile Image', validators=[ FileAllowed(['jpg', 'png']) ])
    staff_role =StringField('Staff Role', validators=[DataRequired()])
    bio = TextAreaField('Student Bio (Optional)')   
    submit = SubmitField('Update')

class advisingNotesForm(FlaskForm):
    academic_comment = StringField('Academic Comment', validators=[DataRequired()])
    next_semester_comment = StringField('Next Semester Comment', validators=[DataRequired()])
    be_advised = BooleanField('Be advised?')
    submit = SubmitField('Approved')

class UpdateStudentAccountForm(FlaskForm):
    EMPLID =IntegerField('EMPLID', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])

    picture = FileField('Update Profile Image', validators=[ FileAllowed(['jpg', 'png']) ])
    bio = TextAreaField('Student Bio (Optional)') # No validators here, since this is completely optional! 
    submit = SubmitField('Update')

    def validate_EMPLID(self, EMPLID):              # checks for duplicate EMPLID's 
        if EMPLID.data != current_user.EMPLID:
            user = User.query.filter_by(EMPLID = EMPLID.data).first()
            if user:
                raise ValidationError('That EMPLID is already in use!')
        
    def validate_email(self, email):                # checks for duplicate emails!
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('The email is already in use!')


class AdvisementForm(FlaskForm):
    semester = SelectField("semester", choices=[("fall", "Fall"), ("spring", "Spring")])
    year = SelectField("year", choices=[(str(year), str(year)) for year in range(date.today().year-1, date.today().year+2)])
    transcript = FileField("Upload Transcript", validators=[ FileAllowed(['pdf']), FileRequired() ])

    course = QuerySelectMultipleField(
        'Course',
        query_factory=lambda: Course.query,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )

    submit = SubmitField('Submit')