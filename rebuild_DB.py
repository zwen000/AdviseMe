from adviseme import db
from adviseme.models import *

db.create_all()


# -- Computer Science:

course_1 = Course(id=1, serial='CSC 10300', name='Intro to CS', type='CSC', description='C++', credits=3)
course_2 = Course(id=2, serial='CSC 10400', name='Discrete Math', type='CSC', description='Fundamental mathematics for CS', credits=4)
course_3 = Course(id=3, serial='CSC 113xx', name='Intro to Python', type='CSC', description='Python', credits=1)
course_4 = Course(id=4, serial='CSC 21100', name='Fundamentals to CS', type='CSC', description='Understanding binary logic', credits=3)
course_5 = Course(id=5, serial='CSC 21200', name='Data Structures', type='CSC', description='Data Structures for algorithms', credits=3)  
course_6 = Course(id=6, serial='CSC 21700', name='Probability and Stats for CS', type='CSC', description='Learn Statistical Analysis', credits=3)  
course_7 = Course(id=7, serial='CSC 22000', name='Algorithms', type='CSC', description='Understanding the use of Data Structures for efficiency', credits=3)  
course_8 = Course(id=8, serial='CSC 22100', name='Software Design Lab', type='CSC', description='Use Java OOP to make GUI', credits=3)  
course_9 = Course(id=9, serial='CSC 30100', name='Numerical Issues', type='CSC', description='Ensuring accuracy using computers', credits=3)
course_10 = Course(id=10, serial='CSC 30400', name='Theoretical CS', type='CSC', description='FSM, PDA, Turing Machines', credits=3)
course_11 = Course(id=11, serial='CSC 32200', name='Software Engineering', type='CSC', description='Learn to use AGILE', credits=4)
course_12 = Course(id=12, serial='CSC 33500', name='Programming Languages Paradigms', type='CSC', description='Use Scheme to learn Functional Programming', credits=3)
course_13 = Course(id=13, serial='CSC 33600', name='Database Systems', type='CSC', description='Learn relational Databases in SQL', credits=3)
course_14 = Course(id=14, serial='CSC 33200', name='Operating Systems', type='CSC', description='Learn the Fundamentals of the Unix Operating System', credits=4)
course_15 = Course(id=15, serial='CSC 34200', name='Computer Organization', type='CSC', description='Learn MIPS, assembly, VHDL', credits=3)
course_16 = Course(id=16, serial='CSC 34300', name='Computer Organ. Lab', type='CSC', description='Apply MIPS, assembly, VHDL', credits=1)
course_17 = Course(id=17, serial='CSC 59866', name='Senior Design I', type='CSC', description=' ', credits=3)
course_18 = Course(id=18, serial='CSC 59867', name='Senior Design II', type='CSC', description=' ', credits=3)


db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)
db.session.add(course_5)
db.session.add(course_6)
db.session.add(course_7)
db.session.add(course_8)
db.session.add(course_9)
db.session.add(course_10)
db.session.add(course_11)
db.session.add(course_12)
db.session.add(course_13)
db.session.add(course_14)
db.session.add(course_15)
db.session.add(course_16)
db.session.add(course_17)
db.session.add(course_18)

db.session.commit()


# -- Mathematics:

course_1 = Course(id=19, serial='MATH 20100', name='Calculus I', type='MATH', description='Understanding relations, variance, and derivatives', credits=3)
course_2 = Course(id=20, serial='MATH 20200', name='Calculus II', type='MATH', description='L hospitals Rule, integrals', credits=3)
course_3 = Course(id=21, serial='MATH 20300', name='Calculus III', type='MATH', description='3 dimensional relations, and integrals', credits=4)
course_4 = Course(id=22, serial='MATH 34600', name='Elements of Linear Algebra', type='MATH', description='Matrix mathematics', credits=3)


db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)

db.session.commit()


# -- Science Electives:

course_1 = Course(id=23, serial='BIO 20100', name='Biological Foundations I', type='BIO', description='Understanding the basics of modern biology', credits=4)
course_2 = Course(id=24, serial='BIO 20200', name='Biological Foundations II', type='BIO', description='Applying the basics of modern biology', credits=4)
course_3 = Course(id=25, serial='CHEM 10300', name='General Chemistry I', type='CHEM', description='Understanding periodic trends', credits=4)
course_4 = Course(id=26, serial='CHEM 10400', name='General Chemistry II', type='CHEM', description='Learning Vanderval interactions', credits=4)
course_5 = Course(id=27, serial='PHY 20700', name='General Physics I', type='PHY', description='Matrix mathematics', credits=4)
course_6 = Course(id=28, serial='PHY 20800', name='General Physics II', type='PHY', description='Matrix mathematics', credits=4)


db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)
db.session.add(course_5)
db.session.add(course_6)

db.session.commit()


# -- Grade  

grade_1 = Grade(id=0, grade='A+', gpa_point=4.0)
grade_2 = Grade(id=1, grade='A', gpa_point=4.0)  
grade_3 = Grade(id=2, grade='A-', gpa_point=3.7) 
grade_4 = Grade(id=3, grade='B+', gpa_point=3.3) 
grade_5 = Grade(id=4, grade='B', gpa_point=3.0)  
grade_6 = Grade(id=5, grade='B-', gpa_point=2.7) 
grade_7 = Grade(id=6, grade='C+', gpa_point=2.3) 
grade_8 = Grade(id=7, grade='C', gpa_point=2.0)  
grade_9 = Grade(id=8, grade='C-', gpa_point=1.7) 
grade_10 = Grade(id=9, grade='D+', gpa_point=1.3) 
grade_11 = Grade(id=10, grade='D', gpa_point=1.0)  
grade_12 = Grade(id=11, grade='F', gpa_point=0.0)
grade_13 = Grade(id=12, grade='W', gpa_point=0.0)
grade_14 = Grade(id=13, grade='WN', gpa_point=0.0)
grade_15 = Grade(id=14, grade='INC', gpa_point=0.0)


db.session.add(grade_1)
db.session.add(grade_2) 
db.session.add(grade_3) 
db.session.add(grade_4) 
db.session.add(grade_5) 
db.session.add(grade_6) 
db.session.add(grade_7) 
db.session.add(grade_8) 
db.session.add(grade_9) 
db.session.add(grade_10)
db.session.add(grade_11) 
db.session.add(grade_12) 

db.session.commit()


# -- School 

school_1 = School(id=1, name='The City College of New York')
school_2 = School(id=2, name='Baruch College')
school_3 = School(id=3, name='Kingsborough')
school_4 = School(id=4, name='BMCC')
school_5 = School(id=5, name='College of Statend Island')
school_6 = School(id=6, name='City College of Technology')
school_7 = School(id=7, name='Hunter College')


db.session.add(school_1)
db.session.add(school_2)
db.session.add(school_3)
db.session.add(school_4)
db.session.add(school_5)
db.session.add(school_6)
db.session.add(school_7)
 
db.session.commit()


# -- Deaprtment 

department_1 = Department(id=1, name='Computer Science')
department_2 = Department(id=2, name='Mathematics')
department_3 = Department(id=3, name='History')
department_4 = Department(id=4, name='Anthropology')
department_5 = Department(id=5, name='Chemistry')
department_6 = Department(id=6, name='Physics')
department_7 = Department(id=7, name='Biology')
department_8 = Department(id=8, name='Art and Humanities')


db.session.add(department_1)
db.session.add(department_2)
db.session.add(department_3)
db.session.add(department_4)
db.session.add(department_5)
db.session.add(department_6)
db.session.add(department_7)
db.session.add(department_8)

db.session.commit()

#-----------------------------------------------------------------
#-----------------------------------------------------------------


# Only use this file by running: 

#------------------------------------
# $ python rebuild_DB.py
#------------------------------------

# This will re-create the DB file. And initialize the Databse with some starting data! 
# Make sure to run this every time any changes are made
# To models.py, before you plan to execute run.py 

