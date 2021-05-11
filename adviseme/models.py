from datetime import datetime,date
from adviseme import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    bio = db.Column(db.String(350), nullable=True)
    role = db.Column(db.String(30), nullable=False)
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'),db.ForeignKey('faculty.EMPLID'))

    def __repr__(self):
        return f"User('{self.email}')"


class Faculty(db.Model):
    EMPLID =db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    staff_role =db.Column(db.String(30), nullable=False)
    User = db.relationship('User', backref='FacultyOwner', lazy=True)
    Notes = db.relationship('Notes', backref='Reviewer', lazy=True)

    def __repr__(self):
        return f"Faculty('{self.EMPLID}')"


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # faculty advisor data stored
    semester = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today())    # to store the exact day on current semester
    academic_comment = db.Column(db.Text, nullable=False, default='')       # comment for academic from advising notes
    next_semester_comment = db.Column(db.Text, nullable=False, default='')  # comment for next semester
    q3 = db.Column(db.Boolean, nullable=False, default=False)
    be_advised = db.Column(db.Boolean, default=None)       # boolean check for notes if it's done

    # no.4 question boolean check
    tutorial = db.Column(db.Boolean, nullable=False, default=False)         # tutorial services
    counseling = db.Column(db.Boolean, nullable=False, default=False)       # counseling
    consultation = db.Column(db.Boolean, nullable=False, default=False)     # faculty consultation
    career = db.Column(db.Boolean, nullable=False, default=False)           # career advisement
    scholarships = db.Column(db.Boolean, nullable=False, default=False)     # scholarship
    internship = db.Column(db.Boolean, nullable=False, default=False)       # internship oppotunities
    followup = db.Column(db.Boolean, nullable=False, default=False)         # follow-up advisement sessions
    # academic advisor data stored
    academic_note = db.Column(db.Text, nullable=False, default='')          # after notes are done by faculty then send to academic advisor
    additional = db.Column(db.Text, nullable=False, default='')             # additional suggest/comment from academic advisor
    approval = db.Column(db.Boolean, default=None)         # check if it's done by advisor
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'), nullable=False)

    FacultyEMPLID = db.Column(db.Integer,db.ForeignKey('faculty.EMPLID'), nullable=True)    # separate student and faculty ID!!!
    Student = db.relationship('Student', backref='advisingnote', lazy=True)

    def __repr__(self):
        return f"Notes('{self.EMPLID}','{self.academic_comment}','{self.next_semester_comment}','{self.be_advised}', '{self.semester}', '{self.year}','{self.be_advised}','{self.approval}' )"



class Enrollement(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.EMPLID'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    grade = db.Column(db.String(15), default='')
    GPA_point = db.Column(db.Integer)
    QPA_point = db.Column(db.Integer)
    component = db.Column(db.Boolean, nullable=True)
    attempt = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    passed = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    student = db.relationship('Student', back_populates='courses', lazy=True)
    course = db.relationship('Course', back_populates='students', lazy=True)

    def __repr__(self):
        return f"Enrollment('{self.student_id}, {self.course_id}, {self.grade}')"

class Student(db.Model):
    EMPLID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    credit_earned=db.Column(db.Integer, unique=False, nullable=False, default=0)
    credit_taken=db.Column(db.Integer, unique=False, nullable=False, default=0)
    graduating = db.Column(db.Boolean, nullable=False, default=False)
    needs_advising = db.Column(db.Boolean, nullable=False, default=False)
    transcript = db.Column(db.String(55), nullable=False, default='Computer_Science.pdf')
    GPA = db.Column(db.Integer, unique=False, nullable=True)
    QPA = db.Column(db.Integer, unique=False, nullable=True)
    Notes = db.relationship('Notes', backref='Owner', lazy=True)
    user = db.relationship('User', backref='studentOwner', lazy=True)

    courses = db.relationship('Enrollement', back_populates='student', lazy=True)

    def __repr__(self):
        return f"Student('{self.EMPLID}, {self.firstname}, {self.lastname}, {self.credit_earned}, {self.credit_taken}, {self.graduating}')"



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)                                    # Auto-increment Primary Key
    serial = db.Column(db.String(15), unique=True, nullable=False)                  # "CSC 103", "CSC 104", "CSC 212"
    name = db.Column(db.String(255), nullable=False)                                # Intro to CS, Discrete Math, Data Structures
    dept = db.Column(db.String(30), nullable=False)                                 # Course type: MATH, CSC, HIST, JWST, etc 
    description = db.Column(db.String(255), nullable=False)                         # C++, Learn Discrete math, etc ... 
    semester = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    designation = db.Column(db.String(255), unique=False, nullable=False)           # Course Designation: "Liberal Art", "A/B/C Group - Technical Elective", "Core Requirement", etc
    credits = db.Column(db.Integer, nullable=False, default=0)
    
    students = db.relationship('Enrollement', back_populates='course', lazy=True)

    def __repr__(self):
        return f"Course('{self.id}','{self.serial}','{self.name}','{self.dept}','{self.description}','{self.credits}')"


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)                        # Auto-increment Primary Key
    value = db.Column(db.String(15))

class Editworkflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    under_advisement = db.Column(db.Boolean, nullable=False, default=True)
    under_faculty = db.Column(db.Boolean, nullable=False, default=False)
    under_academic = db.Column(db.Boolean, nullable=False, default=True)
    under_enrollment = db.Column(db.Boolean, nullable=False, default=True)

    above_advisement = db.Column(db.Boolean, nullable=False, default=True)
    above_faculty = db.Column(db.Boolean, nullable=False, default=True)
    above_academic = db.Column(db.Boolean, nullable=False, default=True)
    above_enrollment = db.Column(db.Boolean, nullable=False, default=True)