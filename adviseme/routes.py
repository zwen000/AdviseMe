from flask import render_template, url_for, flash, redirect, request
from adviseme import app, bcrypt, db
from adviseme.forms import RegistrationForm, LoginForm, advisingNotesForm, StudentInfoForm, FacultyInfoForm
from adviseme.models import User, Student, Faculty, Notes
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def landing():
    return render_template('index.html', title="Welcome!")

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template("about.html", title="About")

# Can register both students and faulties (only ccny or citymail email can sign up.)
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

# Can login both students and faulties, if '@ccny.cuny.edu' would be faculty account, and '@citymail.cuny.edu' should be student account.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                                                          
    if form.validate_on_submit():                                                               
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            if '@citymail.cuny.edu' in user.email and current_user.EMPLID == None:
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('studentinfo_fill'))
            if '@ccny.cuny.edu' in user.email and current_user.EMPLID == None:
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('facultyinfo_fill'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

# Student fill out the basic info on the first time once they signed in
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
    return render_template('studentinfo_fill.html', title='Student Form', form=form)

# Faculty fill out the basic info on the first time once they signed in
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
    return render_template('facultyinfo_fill.html', title='Faculty Form', form=form)

# function for logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# Student can view all notes in this advisingNotesHome route
@app.route('/advisingNotesHome')
@login_required
def advisingNotesHome():
    EMPLID=current_user.EMPLID
    notes=Notes.query.filter_by(EMPLID=EMPLID).all()
    return render_template('advisingNotesHome.html',notes=notes)

# can view the direct note by clicking on the note if below 45 credits only see academic notes
@app.route('/advisingNotes/<int:note_id>')
@login_required
def advisingNotes(note_id):
    notes=Notes.query.get_or_404(note_id)
    return render_template('advisingNotes.html', title='advisingNotes',notes=notes)

# faculty can see all the advising notes from students
# if user is academic advisor, only see students' note below 45 credits.
# elif user is faculty advisor, will see students' note above 45 credits
@app.route('/AdvisingHome')
@login_required
def AdvisingHome():
    notes=Notes.query.all()
    return render_template('AdvisingHome.html',notes=notes)

# faculty can go editing the direct advising note in this route
@app.route('/academicAdvising/<int:note_id>', methods=['GET', 'POST'])
@login_required
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
