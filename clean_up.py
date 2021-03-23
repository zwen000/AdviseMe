import os
import sys
import shutil

from adviseme import db
from adviseme.models import *


file = "./adviseme/database.db"

if os.path.isfile(file):
    os.remove(file)                             # Deletes the old 'database.db' file if it exists.
else:    
    print("Error: %s file not found" % file)

shutil.rmtree("./adviseme/__pycache__")         # Deletes '__pycache__' directory and all its contents.

db.create_all()                                 # Create the new 'database.db' file from 'models.py' 


# -- Computer Science:

course_1 = Course(id=1, serial='CSC 10300', name='Intro to CS', dept='CSC', description='C++', designation="Core Requirement", credits=3)
course_2 = Course(id=2, serial='CSC 10400', name='Discrete Math', dept='CSC', description='Fundamental mathematics for CS', designation="Core Requirement", credits=4)
course_3 = Course(id=3, serial='CSC 113xx', name='Intro to Python', dept='CSC', description='Python', designation="Core Requirement", credits=1)
course_4 = Course(id=4, serial='CSC 21100', name='Fundamentals to CS', dept='CSC', description='Understanding binary logic', designation="Core Requirement", credits=3)
course_5 = Course(id=5, serial='CSC 21200', name='Data Structures', dept='CSC', description='Data Structures for algorithms', designation="Core Requirement", credits=3)  
course_6 = Course(id=6, serial='CSC 21700', name='Probability and Stats for CS', dept='CSC', description='Learn Statistical Analysis', designation="Core Requirement", credits=3)  
course_7 = Course(id=7, serial='CSC 22000', name='Algorithms', dept='CSC', description='Understanding the use of Data Structures for efficiency', designation="Core Requirement", credits=3)  
course_8 = Course(id=8, serial='CSC 22100', name='Software Design Lab', dept='CSC', description='Use Java OOP to make GUI', designation="Core Requirement", credits=3)  
course_9 = Course(id=9, serial='CSC 30100', name='Numerical Issues', dept='CSC', description='Ensuring accuracy using computers', designation="Core Requirement", credits=3)
course_10 = Course(id=10, serial='CSC 30400', name='Theoretical CS', dept='CSC', description='FSM, PDA, Turing Machines', designation="Core Requirement", credits=3)
course_11 = Course(id=11, serial='CSC 32200', name='Software Engineering', dept='CSC', description='Learn to use AGILE', designation="Core Requirement", credits=4)
course_12 = Course(id=12, serial='CSC 33500', name='Programming Languages Paradigms', dept='CSC', description='Use Scheme to learn Functional Programming', designation="Core Requirement", credits=3)
course_13 = Course(id=13, serial='CSC 33600', name='Database Systems', dept='CSC', description='Learn relational Databases in SQL', designation="Core Requirement", credits=3)
course_14 = Course(id=14, serial='CSC 33200', name='Operating Systems', dept='CSC', description='Learn the Fundamentals of the Unix Operating System', designation="Core Requirement", credits=4)
course_15 = Course(id=15, serial='CSC 34200', name='Computer Organization', dept='CSC', description='Learn MIPS, assembly, VHDL', designation="Core Requirement", credits=3)
course_16 = Course(id=16, serial='CSC 34300', name='Computer Organ. Lab', dept='CSC', description='Apply MIPS, assembly, VHDL', designation="Core Requirement", credits=1)
course_17 = Course(id=17, serial='CSC 59866', name='Senior Design I', dept='CSC', description='varies by instructor', designation="Core Requirement", credits=3)
course_18 = Course(id=18, serial='CSC 59867', name='Senior Design II', dept='CSC', description='varies by instructor', designation="Core Requirement", credits=3)
course_19 = Course(id=19, serial='CSC 42200', name='Computability', dept='CSC', description='NP Completeness in depth', designation="Group A Technical Elective", credits=3)
course_20 = Course(id=20, serial='CSC 42800', name='Formal Languages and Automata', dept='CSC', description='understanding advanced theoretical models', designation="Group A Technical Elective", credits=3)
course_21 = Course(id=21, serial='CSC 44800', name='Artificial Intelligence', dept='CSC', description='Understand Turing Models of Intelligence', designation="Group A Technical Elective", credits=3)
course_22 = Course(id=22, serial='CSC 45000', name='Combinatorics & Graph Theory', dept='CSC', description='varies by instructor', designation="Group A Technical Elective", credits=3)
course_23 = Course(id=23, serial='CSC 48000', name='Computer Security', dept='CSC', description='Understand the fundamentals of perfect security and cryptography', designation="Group A Technical Elective", credits=3)
course_24 = Course(id=24, serial='CSC 48600', name='Computational Complexity', dept='CSC', description='Computational feasability v.s NP Completeness', designation="Group A Technical Elective", credits=3)
course_25 = Course(id=25, serial='CSC 44000', name='Computational Methods', dept='CSC', description='Learn the methods to efficiently solve numerical issues', designation="Group B Technical Elective", credits=3)
course_26 = Course(id=26, serial='CSC 44200', name='Systems Simulation', dept='CSC', description='How to implement Dynamic system simulations', designation="Group B Technical Elective", credits=3)
course_27 = Course(id=27, serial='CSC 44600', name='Math Optimization Tech', dept='CSC', description='Learn optimal methods for solving complex mathematics', designation="Group B Technical Elective", credits=3)
course_28 = Course(id=28, serial='CSC 47000', name='Image Processing', dept='CSC', description='Learn image processing/enhancement', designation="Group B Technical Elective", credits=3)
course_29 = Course(id=29, serial='CSC 47100', name='Computer Vision', dept='CSC', description='Utilize Neural Networks and deep learning to create visualization models', designation="Group B Technical Elective", credits=3)
course_30 = Course(id=30, serial='CSC 47200', name='Computer Graphics', dept='CSC', description='Use C++, Qt and modern OpenGL to make computer generated images', designation="Group B Technical Elective", credits=3)
course_31 = Course(id=31, serial='CSC 47900', name='Digital Libraries', dept='CSC', description='Learn to make and take advantage of exisiting digital libraries', designation="Group B Technical Elective", credits=3)
course_32 = Course(id=32, serial='CSC 31800', name='Internet Programming', dept='CSC', description='Learn network protocols, and lossless data transmission algorithms', designation="Group C Technical Elective", credits=3)
course_33 = Course(id=33, serial='CSC 41200', name='Computer Networks', dept='CSC', description='Understanding the physical layers of network transmission', designation="Group C Technical Elective", credits=3)
course_34 = Course(id=34, serial='CSC 42000', name='Compiler Construction', dept='CSC', description='Use Pushdown Automatons to traverse Context Free grammar compilers', designation="Group C Technical Elective", credits=3)
course_35 = Course(id=35, serial='CSC 43000', name='Distributed Computing', dept='CSC', description='Learn the fundamentals of a distributed system', designation="Group C Technical Elective", credits=3)
course_36 = Course(id=36, serial='CSC 43500', name='Concurrency in Operating Systems', dept='CSC', description='Intermediate Unix Operating Systems course', designation="Group C Technical Elective", credits=3)
course_37 = Course(id=37, serial='CSC 43800', name='Real-Time Computing Systems', dept='CSC', description='Understanding the fundamentals of real time computing systems', designation="Group C Technical Elective", credits=3)
course_38 = Course(id=38, serial='CSc 47300', name='Website and Web Applications', dept='CSC', description='Full Stack development course in AGILE', designation="Group C Technical Elective", credits=3)


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

course_39 = Course(id=39, serial='MATH 20100', name='Calculus I', dept='MATH', description='Understanding relations, variance, and derivatives', designation="Core Requirement", credits=3)
course_40 = Course(id=40, serial='MATH 20200', name='Calculus II', dept='MATH', description='L hospitals Rule, integrals', designation="Core Requirement", credits=3)
course_41 = Course(id=41, serial='MATH 20300', name='Calculus III', dept='MATH', description='3 dimensional relations, and integrals', designation="Core Requirement", credits=4)
course_42 = Course(id=42, serial='MATH 34600', name='Elements of Linear Algebra', dept='MATH', description='Matrix mathematics', designation="Core Requirement", credits=3)


db.session.add(course_39)
db.session.add(course_40)
db.session.add(course_41)
db.session.add(course_42)

db.session.commit()


# -- Science Electives:

course_43 = Course(id=43, serial='BIO 20100', name='Biological Foundations I', dept='BIO', description='Understanding the basics of modern biology', designation="Science Elective", credits=4)
course_44 = Course(id=44, serial='BIO 20200', name='Biological Foundations II', dept='BIO', description='Applying the basics of modern biology', designation="Science Elective", credits=4)
course_45 = Course(id=45, serial='CHEM 10300', name='General Chemistry I', dept='CHEM', description='Understanding periodic trends', designation="Science Elective", credits=4)
course_46 = Course(id=46, serial='CHEM 10400', name='General Chemistry II', dept='CHEM', description='Learning Vanderval interactions', designation="Science Elective", credits=4)
course_47 = Course(id=47, serial='PHY 20700', name='General Physics I', dept='PHY', description='2 dimensional Kinematics, and Newtons Laws', designation="Science Elective", credits=4)
course_48 = Course(id=48, serial='PHY 20800', name='General Physics II', dept='PHY', description='Sound, Light, Olhms law', designation="Science Elective", credits=4)


db.session.add(course_43)
db.session.add(course_44)
db.session.add(course_45)
db.session.add(course_46)
db.session.add(course_47)
db.session.add(course_48)

db.session.commit()


# -- Grade Options:
grade_1 = Grade(id=1, value='Not Taken')
grade_2 = Grade(id=2, value='Currently_Enrolled')
grade_3 = Grade(id=3, value='A+')
grade_4 = Grade(id=4, value='A')
grade_5 = Grade(id=5, value='A-')
grade_6 = Grade(id=6, value='B+')
grade_7 = Grade(id=7, value='B')
grade_8 = Grade(id=8, value='B-')
grade_9 = Grade(id=9, value='C+')
grade_10 = Grade(id=10, value='C')
grade_11 = Grade(id=11, value='C-')
grade_12 = Grade(id=12, value='D+')
grade_13 = Grade(id=13, value='D')
grade_14 = Grade(id=14, value='F')


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
db.session.add(grade_13) 
db.session.add(grade_14) 


db.session.commit()



#-----------------------------------------------------------------

"""
# Only use this file by running: 

#------------------------------------
# $ python clean_up.py
#------------------------------------

# This will re-create the DB file. And initialize the Databse with some starting data! 
# Make sure to run this every time any changes are made
# To models.py, before you plan to execute run.py 

"""

#-----------------------------------------------------------------