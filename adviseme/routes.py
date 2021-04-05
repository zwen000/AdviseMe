import os
import math
import secrets
from datetime import date
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from adviseme import app, bcrypt, db
from adviseme.forms import *
from adviseme.models import *
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def landing():
    return render_template('index.html', title="Welcome!")


@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about/')
def about():
    return render_template("about.html", title="About")


# Can register both students and faulties (only ccny or citymail email can sign up.)
@app.route('/register/', methods=['GET', 'POST'])
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
            user = User(email=form.email.data, password=hashed_password, role=role)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            flash('Enter your citymail Please!', 'danger')
    return render_template('register.html', title='Register', form=form)


# Can login both students and faulties, if '@ccny.cuny.edu' would be faculty account, and '@citymail.cuny.edu' should be student account.
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('studentinfo_fill'))

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
                          graduating=form.graduating.data)
        current_user.EMPLID=form.EMPLID.data
        current_user.bio=form.bio.data
        db.session.add(student)
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('courseinfo_fill'))

    return render_template('studentinfo_fill.html', title='Student Form', profile_image=profile_image, form=form)


@app.route('/student/course/info', methods=['GET', 'POST'])
def student_course_info():
    form = CourseCreationForm()
    student_info = Enrollement.query.filter_by(student_id=current_user.EMPLID)
    
    courses = []
    for courseObj in student_info:
        # print(courseObj.grade)
        courses += Course.query.filter_by(id=courseObj.course_id)

    

    for i in courses:
        print(i)
    

    if form.validate_on_submit():
        course = Course(    serial=form.serial.data, 
                            name=form.name.data, 
                            dept=form.dept.data, 
                            description=form.description.data, 
                            designation=form.designation.data,
                            credits=form.credits.data)
        db.session.add(course)
        flash('Your course has been created!', 'success')
        db.session.commit()
        return redirect(url_for('student_course_info'))

    return render_template('student_course_info.html', student_info=student_info, courses=courses, form=form)


all_grade=[]
def stored_grade(alist):
    all_grade.append(alist)
    return all_grade


def remove_list():
    for tup in list(all_grade):
        if tup[2] == current_user.EMPLID:
            all_grade.remove(tup)                                        # Clear the list when all data store into db

def GPA_QPA():
    num_of_courses = Enrollement.query.filter_by(student_id=current_user.EMPLID).count() 
    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
    scores = Enrollement.query.filter_by(student_id=current_user.EMPLID).all()
    student.GPA = 0     # This is the default initial value in the DB anyway 
    
    for score in scores:
        if score.GPA_point:
            student.GPA += int(score.GPA_point)

    if num_of_courses == 0:             # divide by zero error check! 
        print("No classes added yet!")
    else:
        print("The GPA should be: ", student.GPA, "/", num_of_courses, " = ", student.GPA/num_of_courses )    
        student.GPA /= student.credit_earned
        student.GPA = round(student.GPA,3)
        db.session.commit()

    student.QPA = 0
    for value in scores:
        if value.QPA_point:
            if value.course_id >= 1:
                student.QPA += int(value.QPA_point)         # course_id (1-38) in the database are all CS courses!  
            elif value.course_id >= 38:
                student.QPA += 0
                print("id 19 and above are not CS courses!")
            else:
                student.QPA += 0
                print("There cannot be any id's less than 0 or infinity!")

    print("The QPA should be: ", student.QPA)    
    db.session.commit()


@app.route('/course/info', methods=['GET', 'POST'])
@login_required
def courseinfo_fill():
    form = SubmitForm()
    course_form = ElectiveForm()
    courses = Course.query.all()
    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()

    # course_form.elective.choices = [(option.serial) for option in Course.query.filter_by(designation="Liberal Art")]

    if form.validate_on_submit():
        for course_id,grade,EMPLID in all_grade:
            if EMPLID == current_user.EMPLID:
                course = Course.query.get_or_404(course_id)
                print(course_id,grade)
                enrollement = Enrollement.query.filter_by(
                                        student_id=current_user.EMPLID,
                                        course_id = course_id).first()
        
                if not enrollement:
                    enrollement = Enrollement(student_id=current_user.EMPLID,
                                            course_id = course_id,
                                            grade = grade)
                    if grade == '':
                        pass
                    elif grade =='IP':
                        student.credit_taken += course.credits
                        enrollement.attempt = True
                    else:
                        enrollement.GPA_point = int(course.credits*evaluate_GPA(grade))
                        if course_id < 19 :
                            enrollement.QPA_point = evaluate_QPA(grade)
                        else:
                            enrollement.QPA_point = 0 

                        if grade == "F":
                            student.credit_earned += 0
                            enrollement.attempt = True
                            enrollement.passed = False
                        else:
                            student.credit_earned += course.credits
                            enrollement.attempt = True
                            enrollement.passed = True

                    db.session.add(enrollement)
                    db.session.commit()
                elif enrollement.grade == grade:                              # Skip the case of course grade remains the same
                    continue               
                else:
                    if grade == '':
                        pass
                    elif grade =='IP':
                        student.credit_taken += course.credits
                        enrollement.attempt = True
                    else:
                        if enrollement.attempt == True:
                            if enrollement.passed == False and grade == "F":      # Failed the course the first time, retook it and failed again! (FF)
                                student.credit_earned += 0
                                enrollement.attempt = False
                            elif enrollement.passed == True and grade == "F":     # Passed the course the first time, retook it and got an "F"    (PF)
                                student.credit_earned -= course.credits                     # The first passing grade could have been added by user error!
                                enrollement.passed = False
                                enrollement.attempt = False                                  
                            elif enrollement.passed == False and grade != "F":    # Failed the course the first time, retook it and passed!       (FP)
                                student.credit_earned += course.credits
                                enrollement.passed = True
                            elif enrollement.passed == True and grade != "F":     # Passed the course the first time, retook it and passed again! (PP)
                                student.credit_earned += 0
                            else: 
                                student.credit_earned += 0
                        enrollement.grade = grade
                        enrollement.GPA_point = evaluate_GPA(grade)
                        if course_id < 19:
                            enrollement.QPA_point = evaluate_QPA(grade)
                        else:
                            enrollement.QPA_point = 0
                    db.session.commit()
        remove_list()
        return redirect(url_for('student_profile'))



    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template('course_info_fill.html', title='Course Information', 
                            profile_image=profile_image, 
                            courses=courses, 
                            student=student,
                            all_grade=all_grade, 
                            form=form)


@app.route('/course/info/elective/1000', methods=['GET', 'POST'])
@login_required
def Liberal_Art_1000():
    form = ElectiveForm()
    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
    courses = Course.query.all()

    form.elective.choices = [(course_option.serial) for course_option in Course.query.filter_by(designation="[CE](1000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[WCGI](1000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[IS](1000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[US](1000)")]

    form.grade.choices = [(grade_option.value) for grade_option in Grade.query.all()]
    
    if form.validate_on_submit():

        for course in courses:
            # print(course.serial)
            if course.serial == form.elective.data:
                id = course.id
                print(course.id)            
                for courseid, grade,EMPLID in all_grade:
                    if courseid == id:
                        all_grade.remove((id,grade,EMPLID))

        grades=(id,form.grade.data,current_user.EMPLID)
        stored_grade(grades)

        return redirect(url_for('courseinfo_fill'))
    
    return render_template('Elective_Grade_Form.html', title='Course Information', student=student, form=form)



@app.route('/course/info/elective/2000', methods=['GET', 'POST'])
@login_required
def Liberal_Art_2000():
    form = ElectiveForm()
    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
    courses = Course.query.all()

    form.elective.choices = [(course_option.serial) for course_option in Course.query.filter_by(designation="[CE](2000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[WCGI](2000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[IS](2000)")]
    form.elective.choices += [(course_option.serial) for course_option in Course.query.filter_by(designation="[US](2000)")]

    form.grade.choices = [(grade_option.value) for grade_option in Grade.query.all()]
    
    if form.validate_on_submit():

        for course in courses:
            print(course.serial)
            if course.serial == form.elective.data:
                id = course.id
                print(course.id)
                for courseid, grade, EMPLID in all_grade:
                    if courseid == id:
                        all_grade.remove((id,grade,EMPLID))
        
        grades=(id,form.grade.data,current_user.EMPLID)
        stored_grade(grades)
        
        return redirect(url_for('courseinfo_fill'))
    
    return render_template('Elective_Grade_Form.html', title='Course Information', student=student, form=form)




def evaluate_QPA(grade):
    switcher = {
        "A+": 2.0,
        "A": 2.0,
        "A-": 2.0,
        "B+": 1.0,
        "B": 1.0,
        "B-": 1.0,
        "C+": 0.0,
        "C": 0.0,
        "C-": 0.0,
        "D+": -1.0,
        "D": -1.0,
        "F": -2.0,
    }

    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(grade, "Not_Taken") 


def evaluate_GPA(grade):
    switcher = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0,
    }

    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(grade, "Not_Taken") 

#@app.route('/course/info/edit/<int:course_id>', methods=['GET', 'POST'])
#@login_required
#def courseinfo_edit(course_id):
#    form = CourseInfoForm()
#    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
#    course = Course.query.get_or_404(course_id)
#
#    form.grade.choices = [(option.value) for option in Grade.query.all()]
#
#    if form.validate_on_submit():
#        enrollement = Enrollement.query.filter_by(
#                                    student_id=current_user.EMPLID,
#                                    course_id = course.id).first()
#        
#        if not enrollement:
#            enrollement = Enrollement(student_id=current_user.EMPLID,
#                                    course_id = course.id,
#                                    grade = form.grade.data,
#                                    GPA_point = int(course.credits*evaluate_GPA(form.grade.data)),
#                                    attempt=True)
#            if course.id < 19:
#                enrollement.QPA_point = evaluate_QPA(form.grade.data)
#            else:
#                enrollement.QPA_point = 0 
#
#            db.session.add(enrollement)
#
#            if form.grade.data == "F":
#                student.credit_earned += 0
#                enrollement.attempt = True
#                enrollement.passed = False
#            else:
#                student.credit_earned += course.credits
#                enrollement.attempt = True
#                enrollement.passed = True
#            db.session.commit()                
#        else:
#            if enrollement.attempt == True:
#                if enrollement.passed == False and form.grade.data == "F":      # Failed the course the first time, retook it and failed again! (FF)
#                    student.credit_earned += 0
#                elif enrollement.passed == True and form.grade.data == "F":     # Passed the course the first time, retook it and got an "F"    (PF)
#                    student.credit_earned -= course.credits                     # The first passing grade could have been added by user error!
#                    enrollement.passed = False                                  
#                elif enrollement.passed == False and form.grade.data != "F":    # Failed the course the first time, retook it and passed!       (FP)
#                    student.credit_earned += course.credits
#                    enrollement.passed = True
#                elif enrollement.passed == True and form.grade.data != "F":     # Passed the course the first time, retook it and passed again! (PP)
#                    student.credit_earned += 0
#                else: 
#                    student.credit_earned += 0
#
#            enrollement.grade = form.grade.data
#            enrollement.GPA_point = evaluate_GPA(form.grade.data)
#            if course.id < 19:
#                enrollement.QPA_point = evaluate_QPA(form.grade.data)
#            else:
#                enrollement.QPA_point = 0
#            db.session.commit()
#        
#        return redirect(url_for('courseinfo_fill'))
#
#    return render_template('course_info_edit.html', title='Course Information', student=student, form=form)

@app.route('/course/info/edit/<int:course_id>', methods=['GET', 'POST'])
@login_required
def courseinfo_edit(course_id):
    form = CourseInfoForm()
    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
    course = Course.query.get_or_404(course_id)

    form.grade.choices = [(option.value) for option in Grade.query.all()]

    if form.validate_on_submit():
        grades=(course_id,form.grade.data,current_user.EMPLID)
        for id, grade,EMPLID in all_grade:
            if course_id == id and EMPLID == current_user.EMPLID :
                all_grade.remove((id,grade,EMPLID))
        stored_grade(grades)
        
        return redirect(url_for('courseinfo_fill'))

    return render_template('course_info_edit.html', title='Course Information', student=student,course=course, form=form)


# Faculty fill out the basic info on the first time once they signed in
@app.route('/facultyinfo_fill/', methods=['GET', 'POST'])
def facultyinfo_fill():
    form = FacultyInfoForm()
    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)

    if form.validate_on_submit():
        if form.picture.data:                                   # If there exists valid form picture data (i.e .png, .jpg file)
            picture_file = save_picture(form.picture.data)      # Save the image!
            current_user.profile_image = picture_file           # Update the current user profile photo in the database!
            print("Execution Complete!")

        faculty = Faculty(EMPLID=form.EMPLID.data,
                          firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          staff_role=form.staff_role.data)
        db.session.add(faculty)
        current_user.EMPLID = form.EMPLID.data
        db.session.commit()
        flash('Info Updated', 'success')
        return redirect(url_for('faculty'))

    return render_template('facultyinfo_fill.html', title='Faculty Form', profile_image=profile_image, form=form)


# function for logout
@app.route('/logout')
def logout():
    remove_list()
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
        db.session.commit()                                     # commit changes to the database!
        flash('Your account info has been updated successfully!', 'success')
        return redirect(url_for('student_profile'))
    elif request.method == 'GET':
        form.EMPLID.data = current_user.EMPLID
        form.email.data = current_user.email
        form.bio.data = current_user.bio
        form.firstname.data = student.firstname
        form.lastname.data = student.lastname

    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template("student_profile_edit.html", title="Student Profile Edit", profile_image=profile_image, form=form)


@app.route('/student/profile', methods=['GET', 'POST'])
@login_required
def student_profile():
    GPA_QPA()
    form = UpdateStudentAccountForm()
    remove_list()

    if form.validate_on_submit():
        if form.picture.data:                                   # If there exists valid form picture data (i.e .png, .jpg file)
            picture_file = save_picture(form.picture.data)      # Save the image!
            current_user.profile_image = picture_file           # Update the current user profile photo in the database!

        current_user.EMPLID = form.EMPLID.data
        current_user.email = form.email.data
        db.session.commit()  # commit changes to the database!
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
    courses = Course.query.all()
    cs_courses = Course.query.filter_by(dept='CSC').all()
    lib_req_courses = Course.query.filter_by(designation ="Required Liberal Art").all()
    science_courses = []
    for sciences in courses:
        if sciences.id >= 43 and sciences.id <= 48:
            science_courses +=  Course.query.filter_by(id=sciences.id)

    math_courses = Course.query.filter_by(dept='MATH').all()
    student_info = Enrollement.query.filter_by(student_id=current_user.EMPLID)
    
    courses_array = []
    for courseObj in student_info:
        # print(courseObj)
        courses_array += Course.query.filter_by(id=courseObj.course_id)
    
    """
    for i in courses_array:
        print(i)
    """

    student = Student.query.filter_by(EMPLID=current_user.EMPLID).first()
    scores = Enrollement.query.filter_by(student_id=current_user.EMPLID).all()
    #progress bar for Computer Science
    checklistProgressInterval_CS = 100 / 18   # <--- (Instead of 18 you set a variable like CS_count then query and count them)
    CS_width = 0
    for cs_course in cs_courses:
        for score in scores:
            if score.grade and cs_course.id == score.course_id:
                if cs_course.dept == "CSC" and cs_course.id <=18:
                        CS_width += checklistProgressInterval_CS 
    CS_width_num = CS_width/100 * 18

    #progress bar for Computer Science Electives
    checklistProgressInterval_CSE = 100 / 4
    CSE_width = 0
    for cs_elective in courses_array:
        if cs_elective.dept == "CSC" and cs_elective.id > 18:
            CSE_width += checklistProgressInterval_CSE
    CSE_width_num = CSE_width/100 * 4


    #progress bar for Math
    checklistProgressInterval_Math = 100 / 4
    Math_width = 0
    for math_course in courses_array:
        for score in scores:
            if score.grade and math_course.id == score.course_id:
                if math_course.dept == "MATH": 
                    Math_width += checklistProgressInterval_Math
    Math_width_num = Math_width/100 * 4

    #progress bar for Science
    checklistProgressInterval_Science = 100 / 3
    Science_width = 0
    for science_elective in science_courses:
        for score in scores:
            if score.grade and science_elective.id == score.course_id:
                Science_width += checklistProgressInterval_Science
    Science_width_num = Science_width/100 * 3

    #progress bar for Technical Electives
    checklistProgressInterval_TE = 100 / 2
    Tech_width = 0
    tech_courses = []
    #Need to fix to cater to technical electives
    for tech_elective in tech_courses:
        for score in scores:
            if score.grade and tech_elective.id == score.course_id:
                Science_width += checklistProgressInterval_TE
    Tech_width_num = Tech_width/100 * 2

    #progress bar for Flexible Pathways
    checklistProgressInterval_Art = 100 / 4
    Art_width = 0
    for liberal_art_course in courses_array:
        if liberal_art_course.designation == "[IS](1000)" or liberal_art_course.designation == "[IS](2000)" or liberal_art_course.designation == "[WCGI](1000)" or liberal_art_course.designation == "[WCGI](2000)" or liberal_art_course.designation == "[US](1000)" or liberal_art_course.designation == "[US](2000)" or liberal_art_course.designation == "[CE](1000)" or liberal_art_course.designation == "[CE](2000)":
            Art_width += checklistProgressInterval_Art
    Art_width_num = Art_width/100 * 4

    #progress bar for Liberal Arts
    checklistProgressInterval_Lib_Art = 100 / 4
    Lib_Art_width = 0
    for liberal_art_course_req in lib_req_courses:
        for score in scores:
            if score.grade and liberal_art_course_req.id == score.course_id:
                Lib_Art_width += checklistProgressInterval_Lib_Art
    Lib_Art_width_num = Lib_Art_width/100 * 4


    #progress bar for free electives
    checklistProgressInterval_FE = 100 / 2
    FE_width = 0
    free_courses = []
    #Need to fix to cater to free electives
    for free_elective in free_courses:
        for score in scores:
            if score.grade and free_elective.id == score.course_id:
                FE_width += checklistProgressInterval_FE
    FE_width_num = FE_width/100 * 2



    profile_image = url_for('static', filename='Profile_Pics/'+ current_user.profile_image)
    return render_template('checklist.html', title='Checklist', 
                            profile_image=profile_image, 
                            courses=courses, 
                            lib_req_courses = lib_req_courses,
                            student=student, 
                            scores=scores, 
                            cs_courses=cs_courses, 
                            science_courses = science_courses,
                            courses_array=courses_array, 
                            math_courses=math_courses,
                            CS_width_num =  int(CS_width_num),
                            CSE_width_num =  int(CSE_width_num),
                            Math_width_num =  int(Math_width_num),
                            Science_width_num = int(Science_width_num),
                            Tech_width_num = int(Tech_width_num),
                            Art_width_num = int(Art_width_num),
                            FE_width_num = int(FE_width_num),
                            Lib_Art_width_num = int(Lib_Art_width_num),
                            CS_width = CS_width,
                            CSE_width = CSE_width,
                            Math_width = Math_width,
                            Science_width = Science_width,
                            Tech_width = Tech_width,
                            Art_width = Art_width,
                            FE_width = FE_width,
                            Lib_Art_width = Lib_Art_width)

@app.route('/faculty/')
@login_required
def faculty():
    profile_image = url_for('static', filename='Profile_Pics/' + current_user.profile_image)
    return render_template("faculty.html", title="Faculty Profile", profile_image=profile_image)

# function to get current semester 
def get_semester(date):
    year = str(date.year)
    m = date.month * 100
    d = date.day
    md = m + d

    if ((md >= 301) and (md <= 531)):
        semester = 'Spring'  # spring
    elif ((md > 531) and (md < 901)):
        semester = 'Summer'  # summer
    elif ((md >= 901) and (md <= 1130)):
        semester = 'Fall'  # fall
    elif ((md > 1130) and (md <= 229)):
        semester = 'Winter'  # winter
    else:
        raise IndexError("Invalid date")

    return semester +" "+ year

# Student can view all notes in this advisingNotesHome route
@app.route('/advisingNotesHome/')
@login_required
def advisingNotesHome():
    EMPLID = current_user.EMPLID
    notes = Notes.query.filter_by(EMPLID=EMPLID).all()
    return render_template('advisingNotesHome.html', notes=notes)


# can view the direct note by clicking on the note if below 45 credits only see academic notes
@app.route('/advisingNotes/<int:note_id>')
@login_required
def advisingNotes(note_id):
    #note = Notes.query.get_or_404(note_id)
    note=Notes.query.filter_by(id=note_id).first()
    return render_template('advisingNotes.html', title='advisingNotes', note=note)



# faculty can see all the advising notes from students
# if user is academic advisor, only see students' note below 45 credits.
# elif user is faculty advisor, will see students' note above 45 credits
@app.route('/AdvisingHome/')
@login_required
def AdvisingHome():
    notes = Notes.query.all()
    return render_template('AdvisingHome.html', notes=notes)


# faculty can go editing the direct advising note in this route
@app.route('/academicAdvising/<int:note_id>', methods=['GET', 'POST'])
@login_required
def academicAdvising(note_id):
    notes = Notes.query.get_or_404(note_id)
    form = advisingNotesForm()
    if form.validate_on_submit():
        notes.academic_comment=form.academic_comment.data
        notes.next_semester_comment=form.next_semester_comment.data
        notes.be_advised=form.be_advised.data
        if notes.Owner.credit_earned <= 45 and form.be_advised.data == True:
            notes.approval = True
        db.session.commit()
        flash('Notes saved!', 'success')
        return redirect(url_for('AdvisingHome'))
    elif request.method == 'GET':
        form.academic_comment.data=notes.academic_comment
        form.next_semester_comment.data=notes.next_semester_comment
        form.be_advised.data=notes.be_advised
    return render_template('academicAdvising.html', title='academicAdvising',notes=notes,form=form)

# academic advisor should review completed advising forms and notes in this page
@app.route('/noteReviewHome')
@login_required
def noteReviewHome():
    notes=Notes.query.filter_by(be_advised=True).all()
    return render_template('noteReviewHome.html',notes=notes)


# academic advisor approve advisement then leave academic notes
@app.route('/noteReview/<int:note_id>', methods=['GET', 'POST'])
@login_required
def noteReview(note_id):
    notes=Notes.query.get_or_404(note_id)
    form = NoteReviewForm()
    if form.validate_on_submit():
        notes.academic_note=form.academic_note.data
        notes.additional=form.additional.data
        notes.approval=form.approval.data
        db.session.commit()
        flash('Confirmed!', 'success')
        return redirect(url_for('noteReviewHome'))
    elif request.method == 'GET':
        form.academic_note.data=notes.academic_note
        form.additional.data=notes.additional
        form.approval.data=notes.approval
    return render_template('noteReview.html', title='noteReview',notes=notes,form=form)

@app.route('/workflow/')
@login_required
def workflow():
    return render_template('workflow.html', title="workflow")

@app.route('/Advisement', methods=['GET', 'POST'])
@login_required
def Advisement():
    form = AdvisementForm()
    GPA_QPA()

    enrolled = {i.course_id: i.grade for i in current_user.studentOwner.courses}
    course_obj = {i[0]:i[1] for i in form.course.iter_choices()} # checkbox_field_id: course_object

    if form.validate_on_submit():
        for course in form.course.data:
            enrollement = Enrollement.query.filter_by(
                                        student_id=current_user.EMPLID,
                                        course_id = course.id).first()
            if not enrollement:                              
                enrollement = Enrollement(student_id=current_user.EMPLID,
                                        course_id = course.id,
                                        attempt = True)
                db.session.add(enrollement)
            else:
                enrollement.grade = ''
                enrollement.attempt = True
        note = Notes(EMPLID=current_user.EMPLID)   
        db.session.add(note)
        db.session.commit()        
        return redirect(url_for('student_profile'))                           


    return render_template('AdvisementForm.html', title="Live Advisement Form", form=form, enrolled=enrolled, course_obj=course_obj)
