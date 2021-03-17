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

course_1 = Course(id=1, serial='CSC 10300', name='Intro to CS', dept='CSC', description='C++', credits=3)
course_2 = Course(id=2, serial='CSC 10400', name='Discrete Math', dept='CSC', description='Fundamental mathematics for CS', credits=4)
course_3 = Course(id=3, serial='CSC 113xx', name='Intro to Python', dept='CSC', description='Python', credits=1)
course_4 = Course(id=4, serial='CSC 21100', name='Fundamentals to CS', dept='CSC', description='Understanding binary logic', credits=3)
course_5 = Course(id=5, serial='CSC 21200', name='Data Structures', dept='CSC', description='Data Structures for algorithms', credits=3)  
course_6 = Course(id=6, serial='CSC 21700', name='Probability and Stats for CS', dept='CSC', description='Learn Statistical Analysis', credits=3)  
course_7 = Course(id=7, serial='CSC 22000', name='Algorithms', dept='CSC', description='Understanding the use of Data Structures for efficiency', credits=3)  
course_8 = Course(id=8, serial='CSC 22100', name='Software Design Lab', dept='CSC', description='Use Java OOP to make GUI', credits=3)  
course_9 = Course(id=9, serial='CSC 30100', name='Numerical Issues', dept='CSC', description='Ensuring accuracy using computers', credits=3)
course_10 = Course(id=10, serial='CSC 30400', name='Theoretical CS', dept='CSC', description='FSM, PDA, Turing Machines', credits=3)
course_11 = Course(id=11, serial='CSC 32200', name='Software Engineering', dept='CSC', description='Learn to use AGILE', credits=4)
course_12 = Course(id=12, serial='CSC 33500', name='Programming Languages Paradigms', dept='CSC', description='Use Scheme to learn Functional Programming', credits=3)
course_13 = Course(id=13, serial='CSC 33600', name='Database Systems', dept='CSC', description='Learn relational Databases in SQL', credits=3)
course_14 = Course(id=14, serial='CSC 33200', name='Operating Systems', dept='CSC', description='Learn the Fundamentals of the Unix Operating System', credits=4)
course_15 = Course(id=15, serial='CSC 34200', name='Computer Organization', dept='CSC', description='Learn MIPS, assembly, VHDL', credits=3)
course_16 = Course(id=16, serial='CSC 34300', name='Computer Organ. Lab', dept='CSC', description='Apply MIPS, assembly, VHDL', credits=1)
course_17 = Course(id=17, serial='CSC 59866', name='Senior Design I', dept='CSC', description=' ', credits=3)
course_18 = Course(id=18, serial='CSC 59867', name='Senior Design II', dept='CSC', description=' ', credits=3)


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

course_1 = Course(id=19, serial='MATH 20100', name='Calculus I', dept='MATH', description='Understanding relations, variance, and derivatives', credits=3)
course_2 = Course(id=20, serial='MATH 20200', name='Calculus II', dept='MATH', description='L hospitals Rule, integrals', credits=3)
course_3 = Course(id=21, serial='MATH 20300', name='Calculus III', dept='MATH', description='3 dimensional relations, and integrals', credits=4)
course_4 = Course(id=22, serial='MATH 34600', name='Elements of Linear Algebra', dept='MATH', description='Matrix mathematics', credits=3)


db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)

db.session.commit()


# -- Science Electives:

course_1 = Course(id=23, serial='BIO 20100', name='Biological Foundations I', dept='BIO', description='Understanding the basics of modern biology', credits=4)
course_2 = Course(id=24, serial='BIO 20200', name='Biological Foundations II', dept='BIO', description='Applying the basics of modern biology', credits=4)
course_3 = Course(id=25, serial='CHEM 10300', name='General Chemistry I', dept='CHEM', description='Understanding periodic trends', credits=4)
course_4 = Course(id=26, serial='CHEM 10400', name='General Chemistry II', dept='CHEM', description='Learning Vanderval interactions', credits=4)
course_5 = Course(id=27, serial='PHY 20700', name='General Physics I', dept='PHY', description='Matrix mathematics', credits=4)
course_6 = Course(id=28, serial='PHY 20800', name='General Physics II', dept='PHY', description='Matrix mathematics', credits=4)


db.session.add(course_1)
db.session.add(course_2)
db.session.add(course_3)
db.session.add(course_4)
db.session.add(course_5)
db.session.add(course_6)

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