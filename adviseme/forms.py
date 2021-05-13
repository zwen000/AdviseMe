from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
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


class FacultySearchStudentForm(FlaskForm):
    EMPLID = IntegerField('EMPLID')
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    filters = SelectField('Filter', choices=[])
    submit = SubmitField('Search')


class SubmitForm(FlaskForm):
    submit = SubmitField('Submit')
    
class CourseInfoForm(FlaskForm):
    grade = SelectField('grade: ', choices=[])
    submit = SubmitField('Submit')


class CourseForm(FlaskForm):

    choices = ['Core Requirement', 'Group A Elective', 'Group B Elective', 
                'Group C Elective', 'Science Elective', 'Required Liberal Art', 
                '[CE](1000)', '[WCGI](1000)', '[IS](1000)', '[US](1000)', 
                '[CE](2000)', '[WCGI](2000)', '[IS](2000)', '[US](2000)', 
                'Technical Elective']

    dept_options = ['CSC', 'MATH','BIO', 'CHEM', 'PHY', 'ENGL', 'THEATRE/SPEECH', 
                    'ECO', 'ENGR', 'ART', 'MUS', 'JWST', 'ANTH', 'ASIA', 'BLST',
                    'HIST', 'LIB', 'PSY', 'SOC', 'WS', 'PSC', 'USSO', 'PHIL', 
                    'AES', 'URB', 'FREN', 'SPAN', 'EDCE', 'EAS', 'Arbitrary']

    serial = StringField('Course Serial:', validators=[DataRequired()])
    course_name = StringField('Course Name:', validators=[DataRequired()])
    dept = SelectField('Department:', choices=dept_options)
    course_description = TextAreaField('Course Description: (Optional)')
    designation = SelectField('Designation:', choices=choices)
    credits = IntegerField('Course Credits:', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # This function checks for duplicate Course Serial's ... there should not be any duplicates. 
    def validate_Serial(self, serial):               
        course = Course.query.filter_by(serial=serial.data).first()
        if course:
            raise ValidationError('A course by that name already exists!')



# course_count = db.session.query(Course.id).count()     # This is a more OPTIMAL method of doing this!!! 
# db.session.close()     # If I don't close the session here, running clean_up.py will run into a [win32] Permission Error!

# Refer to --->  https://stackoverflow.com/questions/14754994/why-is-sqlalchemy-count-much-slower-than-the-raw-query 
# As to why this is more optimal for anyone curious enough to read this -- Ray


class Cirriculum_Form(FlaskForm):
    courses = FieldList(FormField(CourseForm), min_entries=0, max_entries=None)  # 126 courses in the DB by default 
    submit = SubmitField('Update Course Info')

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


class AcademicReviewForm(FlaskForm):
    course = QuerySelectMultipleField(
        'Course',
        query_factory=lambda: Course.query,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )

    academic_note = TextAreaField('academic_note', validators=[DataRequired()])
    additional = TextAreaField('additional')
    approval = BooleanField('Approved')
    submit = SubmitField('Viewed')


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
    semester = SelectField("semester", choices=[("SPRING", "Spring"), ("FALL", "Fall")])
    date =date.today()
    year = SelectField("year", choices=[(str(year), str(year)) for year in range(date.today().year, date.today().year+2)])
    date = date.today()
    transcript = FileField("Upload Transcript", validators=[FileAllowed(['pdf']), FileRequired()])

    course = QuerySelectMultipleField(
        'Course',
        query_factory=lambda: Course.query,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )

    tech_elec1 = QuerySelectMultipleField(
        'Technical Elective 1',
        query_factory=lambda: Course.query.filter_by(designation="Technical Elective"),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    tech_elec_check1 = BooleanField('Technical Elective 1')

    tech_elec2 = QuerySelectMultipleField(
        'Technical Elective 2',
        query_factory=lambda: Course.query.filter_by(designation="Technical Elective"),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    tech_elec_check2 = BooleanField('Technical Elective 2')

    CE = QuerySelectMultipleField(
        'Creative Expression',
        query_factory=lambda: Course.query.filter(
            (Course.designation=="[CE](1000)")|(Course.designation=="[CE](2000)")),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    CE_check = BooleanField('Creative Expression')

    USE = QuerySelectMultipleField(
        'US Experience in its Diversity',
        query_factory=lambda: Course.query.filter(
            (Course.designation == "[US](1000)") | (Course.designation == "[US](2000)")),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    USE_check = BooleanField('US Experience in its Diversity')

    IS = QuerySelectMultipleField(
        'Individual and Society',
        query_factory=lambda: Course.query.filter(
            (Course.designation == "[IS](1000)") | (Course.designation == "[IS](2000)")),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    IS_check = BooleanField('Individual and Society')

    WCGI = QuerySelectMultipleField(
        'World Cultures and Global Issues',
        query_factory=lambda: Course.query.filter(
            (Course.designation == "[WCGI](1000)") | (Course.designation == "[WCGI](2000)")),
        allow_blank=True,
        widget=widgets.Select(multiple=False),
        get_label='serial'
    )
    WCGI_check = BooleanField('World Cultures and Global Issues')

    submit = SubmitField('Submit to Advisor')

class FacultyReviewForm(FlaskForm):
    course = QuerySelectMultipleField(
        'Course',
        query_factory=lambda: Course.query,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput()
    )

    q1 = TextAreaField('Advisement Question 1', validators=[DataRequired()])
    q2 = TextAreaField('Advisement Question 2', validators=[DataRequired()])
    q3 = BooleanField('Advisement Question 3')

    tutorial = BooleanField('Tutorial Services')
    counseling = BooleanField('Counseling(Psychological, Financial, Personal, etc)')
    consultation = BooleanField('Faculty Consultation(Office Hours)')
    career = BooleanField('Career Advisement')
    scholarships = BooleanField('Scholarships')
    internship = BooleanField('Internship Opportunities')
    followup = BooleanField('Follow-up Advisement Sessions')

    approve = BooleanField('Approval toggle')
    submit = SubmitField('Viewed')


class EditworkflowForm(FlaskForm):
    under_advisement = BooleanField('Submit Advisement Form')
    under_faculty = BooleanField('Faculty Advisor Approval')
    under_academic = BooleanField('Academic Advisor Approval')
    under_enrollment = BooleanField('Eligible for Enrollment')

    above_advisement = BooleanField('Submit Advisement Form')
    above_faculty = BooleanField('Faculty Advisor Approval')
    above_academic = BooleanField('Academic Advisor Approval')
    above_enrollment = BooleanField('Eligible for Enrollment')
    submit = SubmitField('Update')

