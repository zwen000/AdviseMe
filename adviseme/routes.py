import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from adviseme import app, bcrypt, db
from adviseme.forms import RegistrationForm, LoginForm, advisingNotesForm, StudentInfoForm, FacultyInfoForm, UpdateStudentAccountForm, CourseInfoForm
from adviseme.models import *
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
            if '@citymail.cuny.edu' in form.email.data:
                role = 'Student'
            else:
                role = 'Faculty'
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(email=form.email.data, password=hashed_password,role=role)
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            if current_user.role == 'Student' and current_user.EMPLID == None:
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('studentinfo_fill'))

            elif current_user.role == 'Faculty' and current_user.EMPLID == None:
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('facultyinfo_fill'))
            elif current_user.role == 'Student':
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('student_profile'))
            elif current_user.role == 'Faculty':
                next_page = request.args.get('next')
                flash('Login Successful. Welcome to AdviseMe', 'success')
                return redirect(next_page) if next_page else redirect(url_for('faculty'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)




def save_picture(form_picture):
    random_hex = secrets.token_hex(8)                                               # We don't want to make this too large trust me!
    _, f_ext = os.path.splitext(form_picture.filename)                              # the os module allows us to extract a file's extension
    picture_fn = random_hex + f_ext                                                 # filename = hex value + file extension (.jpg, .png)
    picture_path = os.path.join(app.root_path, 'static/Profile_Pics', picture_fn)   # File/path/to/save/picture!

    # This entire section of the code below just compresses the image to save space on our devices/the hosting sever (once deployed)!
    #-----------------------------------------------
    output_size = (125, 125)
    image_compressed = Image.open(form_picture)
    image_compressed.thumbnail(output_size)
    #-----------------------------------------------

    image_compressed.save(picture_path)                                             # Save the compressed picture to the: 'static/Profile_Pics/'

    return picture_fn


# Student fill out the basic info on the first time once they signed in
@app.route('/studentinfo_fill', methods=['GET', 'POST'])
def studentinfo_fill():
    form = StudentInfoForm()
    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)

    if form.validate_on_submit():
        if form.picture.data:                                   # If there exists valid form picture data (i.e .png, .jpg file)
            picture_file = save_picture(form.picture.data)      # Save the image!
            current_user.profile_image = picture_file           # Update the current user profile photo in the database!
            print("Execution Complete!")

        student = Student(EMPLID=form.EMPLID.data,
                          firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          middlename=form.middlename.data,
                          credit_earned=form.credit_earned.data,
                          credit_taken=form.credit_taken.data,
                          graduating=form.graduating.data)
        note = Notes(EMPLID=form.EMPLID.data)
        current_user.EMPLID=form.EMPLID.data
        current_user.bio=form.bio.data
        db.session.add(student)
        db.session.add(note)
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('student_profile'))

    return render_template('studentinfo_fill.html', title='Student Form', profile_image=profile_image, form=form)



@app.route('/courseinfo_fill', methods=['GET', 'POST'])
def courseinfo_fill():
    form = CourseInfoForm()
    courses = Course.query.all()
    users = User.query.filter_by(EMPLID=current_user.EMPLID).first()

    """
    if form.validate_on_submit():

        course = Course(serial=form.serial.data,
                        name=form.name.data,
                        instructor=form.instructor.data,
                        credits=form.credits.data)
        db.session.add(course)
        course.enrollee.append(current_user.StudentOwner)
        db.session.commit()
        course.enrollee.grade_earned.append(form.grade.data)
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('courseinfo_fill'))
    elif request.method == 'GET':
        print(current_user.StudentOwner)
        print(current_user.CourseOwner)
    """

    return render_template('course_info_fill.html', title='Course Information', courses=courses, form=form, users=users)




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
        return redirect(url_for('faculty'))
    return render_template('facultyinfo_fill.html', title='Faculty Form', form=form)

# function for logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/student/profile/edit', methods=['GET', 'POST'])
@login_required
def student_profile_edit():
    form = UpdateStudentAccountForm()
    EMPLID=current_user.EMPLID
    student = Student.query.filter_by(EMPLID=EMPLID).first()

    if form.validate_on_submit():
        if form.picture.data:                                   # If there exists valid form picture data (i.e .png, .jpg file)
            picture_file = save_picture(form.picture.data)      # Save the image!
            current_user.profile_image = picture_file           # Update the current user profile photo in the database!

        current_user.EMPLID=form.EMPLID.data
        current_user.bio=form.bio.data
        current_user.email = form.email.data
        student.firstname = form.firstname.data
        student.lastname = form.lastname.data
        student.middlename = form.middlename.data
        student.credit_earned = form.credit_earned.data
        student.credit_taken = form.credit_taken.data
        db.session.commit()                                     # commit changes to the database!
        flash('Your account info has been updated successfully!', 'success')
        return redirect(url_for('student_profile'))
    elif request.method == 'GET':
        form.EMPLID.data = current_user.EMPLID
        form.email.data = current_user.email
        form.bio.data = current_user.bio
        form.firstname.data = student.firstname
        form.lastname.data = student.lastname
        form.middlename.data = student.middlename
        form.credit_earned.data = student.credit_earned
        form.credit_taken.data = student.credit_taken

    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template("student_profile_edit.html", title="Student Profile Edit", profile_image=profile_image, form=form)


@app.route('/student/profile', methods=['GET', 'POST'])
@login_required
def student_profile():
    form = UpdateStudentAccountForm()

    if form.validate_on_submit():
        if form.picture.data:                                   # If there exists valid form picture data (i.e .png, .jpg file)
            picture_file = save_picture(form.picture.data)      # Save the image!
            current_user.profile_image = picture_file           # Update the current user profile photo in the database!

        current_user.EMPLID = form.EMPLID.data
        current_user.email = form.email.data
        db.session.commit()                                     # commit changes to the database!
        flash('Your account info has been updated successfully!', 'success')
        return redirect(url_for('student_profile'))
    elif request.method == 'GET':
        form.EMPLID.data = current_user.EMPLID
        form.email.data = current_user.email

    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template("student_profile.html", title="Student Profile", profile_image=profile_image, form=form)

@app.route('/checklist')
@login_required
def checklist():
    return render_template("checklist.html", title="Checklist")

@app.route('/faculty')
@login_required
def faculty():
    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template("faculty.html", title="Faculty Profile", profile_image=profile_image)


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
