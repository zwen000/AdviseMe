from datetime import datetime
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
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'),db.ForeignKey('faculty.EMPLID'))
    bio = db.Column(db.String(350), nullable=True)
    role = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"


class Faculty(db.Model):
    EMPLID =db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), unique=True, nullable=False)
    lastname = db.Column(db.String(30), unique=True, nullable=False)
    middlename =db.Column(db.String(30), nullable=True)
    staff_role =db.Column(db.String(30), nullable=False)
    User = db.relationship('User', backref='FacultyOwner', lazy=True)
    Notes = db.relationship('Notes', backref='Reviewer', lazy=True)

    def __repr__(self):
        return f"Faculty('{self.EMPLID}')"


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semster = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    academic_comment = db.Column(db.Text, nullable=False, default='')
    next_semester_comment = db.Column(db.Text, nullable=False, default='')
    be_advised = db.Column(db.Boolean, nullable=False, default=False)
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'), db.ForeignKey('faculty.EMPLID'), nullable=False)
    Student = db.relationship('Student', backref='advisingnote', lazy=True)

    def __repr__(self):
        return f"Notes('{self.EMPLID}','{self.academic_comment}','{self.next_semester_comment}','{self.be_advised}')"




# This must be a many-to-many relationship:  (We need an associations table)
# One student can take many classes, however a class can be taken my many students! 
enrollements = db.Table('enrollements',
    db.Column('student_id', db.Integer, db.ForeignKey('student.EMPLID')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('grade_id', db.Integer, db.ForeignKey('grade.id'))
)


class Student(db.Model):
    EMPLID =db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    middlename = db.Column(db.String(30), nullable=True)
    credit_earned=db.Column(db.Integer, unique=False, nullable=False,default=0)
    credit_taken=db.Column(db.Integer, unique=False, nullable=False,default=0)
    graduating = db.Column(db.Boolean, nullable=False, default=False)
    Notes = db.relationship('Notes', backref='Owner', lazy=True)
    User = db.relationship('User', backref='StudentOwner', lazy=True)

    enrollement = db.relationship('Course', secondary=enrollements, backref='enrollee', lazy='dynamic')

    def __repr__(self):
        return f"Student('{self.EMPLID}, {self.firstname}, {self.lastname}, {self.middlename}, {self.credit_earned}, {self.credit_taken}, {self.graduating}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # Auto-increment Primary Key
    serial = db.Column(db.String(15), nullable=False)      # "CSC 103", "CSC 104", "CSC 211" 
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    instructor = db.Column(db.String(30), nullable=False)
    credits = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Notes('{self.id}','{self.serial}','{self.name}','{self.description}','{self.instructor}','{self.credits}')"


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # Auto-increment Primary Key
    grade = db.Column(db.String(15), nullable=False)
    
    performance = db.relationship('Student', secondary=enrollements, backref='grade_earned', lazy='dynamic')


