from flask import Flask, render_template, url_for, flash, redirect,request,abort
from forms import RegistrationForm, LoginForm, advisingNotesForm, StudentInfoForm, FacultyInfoForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user,login_required,logout_user
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)


app.config['SECRET_KEY'] = '3a005a74e33b93ce317f78c78fb2577d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'),db.ForeignKey('faculty.EMPLID'))
    Student = db.relationship('Student', backref='account', lazy=True)
    Faculty = db.relationship('Faculty', backref='account', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"


class Student(db.Model):
    EMPLID =db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    middlename =db.Column(db.String(30), nullable=True)
    credit_earned=db.Column(db.Integer, unique=False, nullable=False,default=0)
    credit_taken=db.Column(db.Integer, unique=False, nullable=False,default=0)
    graduating = db.Column(db.Boolean, nullable=False, default=False)
    Notes = db.relationship('Notes', backref='Owner', lazy=True)

    def __repr__(self):
        return f"Student('{self.EMPLID}')"

class Faculty(db.Model):
    EMPLID =db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    middlename =db.Column(db.String(30), nullable=True)
    staff_role =db.Column(db.String(30), nullable=True)
    User = db.relationship('User', backref='FacultyOwner', lazy=True)

    def __repr__(self):
        return f"Faculty('{self.EMPLID}')"


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semster = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    academic_comment = db.Column(db.Text, nullable=False, default='')
    next_semester_comment = db.Column(db.Text, nullable=False, default='')
    be_advised = db.Column(db.Boolean, nullable=False, default=False)
    EMPLID = db.Column(db.Integer, db.ForeignKey('student.EMPLID'), nullable=False)
    Student = db.relationship('Student', backref='advisingnote', lazy=True)

    def __repr__(self):
        return f"Notes('{self.EMPLID}','{self.academic_comment}','{self.next_semester_comment}','{self.be_advised}')"


@app.route('/')
def landing():
    return render_template('index.html', title="Welcome!")

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    team = [
        {
            'name': 'Chrystal Mingo',
            'image': url_for('static', filename="dev_pics/CM.png"),
            'description': "is a senior majoring in Computer Science at The City College of New York. She has interned at various companies such as Verizon, Morgan Stanley, and Citi as a software developer. She also has a passion for teaching and has worked as a Teacher for the Girls Who Code Summer Immersion Program, and taught Algebra I and II, as well as Intro and AP Computer Science courses in Spanish and English at Gregorio Luperon High School. Chrystal Mingo is also a Grace Hopper 2019 Scholarship Recipient, and current President of Women in Computer. She will be graduating from CCNY in Spring 2021 and entering Citi’s EIOT full-time rotational program as a project manager. She is one of the frontend developers for AdviseMe and believes this project will be a game-changer for advisement at CCNY.",
            'git': 'https://github.com/chrystalmingo',
            'linkedin': '',
            'email':''
        },
        {
            'name': 'Zhicong Wen',
            'image': url_for('static', filename="dev_pics/ZW.jpg"),
            'description': "is a senior majoring in Computer Science at City College of New York. Previously he was interning as a Python programmer at the NYC Department of Environmental Protection(DEP). He also worked on Quality Assurance of the New York City sewer system database. He will be graduating from CCNY in Fall 2021. He is one of the frontend developers for AdviseMe.",
            'git': 'https://github.com/zwen000',
            'linkedin': 'https://www.linkedin.com/in/zhicongw-b243a7169/',
            'email': ''
        },
        {
            'name': 'Xunshan Lin',
            'image': url_for('static', filename="dev_pics/XL.jpg"),
            'description': "is a senior majoring in computer engineering at The City College of New York. Previously he was interning as a Python programmer at Mini circuits company. He is beginning to pick up an interest in full-stack development at his senior design project at CCNY. He works as one of the backend developers for AdviseMe and hopes this platform will help students make better academic plans at CCNY.",
            'git': 'https://github.com/linxunshan',
            'linkedin': 'https://www.linkedin.com/in/xunshan-lin-999972205/',
            'email': ''
        },
        {
            'name': 'Rehman Arshad',
            'image': url_for('static', filename="dev_pics/RA.png"),
            'description': "is a senior majoring in Computer Science at The City College of New York. He has interned at various academic research institutions at The Groove school of Engineering, such as NOAA Crest (National Oceanic Atmospheric Administration) and Professor Tarek Sadawi. At NOAA Crest, he worked on data collection and analysis using data from the National Weather Service. With Professor Tarek Sadawi he worked on an IoT medical application that would enable remote patient monitoring as a research assistant. He was a part of CUNY Tech Prep cohort 5, a Full Stack program part of NYC Tech Talent Pipeline. Also, he has a fascination with mathematics and a passion for computer graphics and video game development. He will be graduating from The City College of New York in Fall 2021. He is one of the backend developers for AdviseMe and hopes this online platform can help the next generation of students entering CCNY.",
            'git': 'https://github.com/rehman000',
            'linkedin': 'https://www.linkedin.com/in/rehman-arshad/',
            'email': ''
        },
    ]

    return render_template("about.html", title="About", team=team)

# Can register both students and faulties
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if ('@citymail.cuny.edu' in form.email.data) or ('@ccny.cuny.edu' in form.email.data):
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            flash('Enter your citymail Please!', 'danger')
    return render_template('register.html', title='Register', form=form)

# Can register both students and faulties, if '@ccny.cuny.edu' would be faculty account, and '@citymail.cuny.edu' should be student account
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                                                          
    if form.validate_on_submit():                                                               
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            if '@citymail.cuny.edu' in user.email and current_user.EMPLID == None:
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('studentinfo_fill'))
            if '@ccny.cuny.edu' in user.email and current_user.EMPLID == None:
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('facultyinfo_fill'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

# Student fill out the basic info on the first time
@app.route('/studentinfo_fill', methods=['GET', 'POST'])
def studentinfo_fill():
    form = StudentInfoForm()
    if form.validate_on_submit():
        student = Student(EMPLID=form.EMPLID.data,
                          firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          middlename=form.middlename.data,
                          credit_earned=form.credit_earned.data,
                          credit_taken=form.credit_taken.data,
                          graduating=form.graduating.data)
        note = Notes(EMPLID=form.EMPLID.data)
        current_user.EMPLID=form.EMPLID.data
        db.session.add(student)
        db.session.add(note)
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('home'))
    return render_template('studentinfo_fill.html', title='info_fill', form=form)

# Faculty fill out the basic info on the first time
@app.route('/facultyinfo_fill', methods=['GET', 'POST'])
def facultyinfo_fill():
    form = FacultyInfoForm()
    if form.validate_on_submit():
        faculty = Faculty(EMPLID=form.EMPLID.data,
                          firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          middlename=form.middlename.data,
                          staff_role=form.staff_role.data)
        db.session.add(faculty)
        current_user.EMPLID=form.EMPLID.data
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('home'))
    return render_template('facultyinfo_fill.html', title='info_fill', form=form)

# function for logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# Student can view all notes in this route
@app.route('/advisingNotesHome')
def advisingNotesHome():
    EMPLID=current_user.EMPLID
    notes=Notes.query.filter_by(EMPLID=EMPLID).all()
    return render_template('advisingNotesHome.html',notes=notes)

# Can view the direct note 
@app.route('/advisingNotes/<int:note_id>')
def advisingNotes(note_id):
    notes=Notes.query.get_or_404(note_id)
    return render_template('advisingNotes.html', title='advisingNotes',notes=notes)

#faculty can see all the advising notes from students
@app.route('/AdvisingHome')
def AdvisingHome():
    notes=Notes.query.all()
    return render_template('AdvisingHome.html',notes=notes)

#faculty can go editing the direct advising note in this route
@app.route('/academicAdvising/<int:note_id>', methods=['GET', 'POST'])
def academicAdvising(note_id):
    notes=Notes.query.get_or_404(note_id)
    form = advisingNotesForm()
    if form.validate_on_submit():
        notes.academic_comment=form.academic_comment.data
        notes.next_semester_comment=form.next_semester_comment.data
        notes.be_advised=form.be_advised.data
        db.session.commit()
        flash('Notes saved!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.academic_comment.data=notes.academic_comment
        form.next_semester_comment.data=notes.next_semester_comment
        form.be_advised.data=notes.be_advised
    return render_template('academicAdvising.html', title='academicAdvising',notes=notes,form=form)


if __name__ == '__main__':
    app.run(debug=True)
