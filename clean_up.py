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
course_19 = Course(id=19, serial='CSC 42200', name='Computability', dept='CSC', description='NP Completeness in depth', designation="Group A Elective", credits=3)
course_20 = Course(id=20, serial='CSC 42800', name='Formal Languages and Automata', dept='CSC', description='understanding advanced theoretical models', designation="Group A Elective", credits=3)
course_21 = Course(id=21, serial='CSC 44800', name='Artificial Intelligence', dept='CSC', description='Understand Turing Models of Intelligence', designation="Group A Elective", credits=3)
course_22 = Course(id=22, serial='CSC 45000', name='Combinatorics & Graph Theory', dept='CSC', description='varies by instructor', designation="Group A Elective", credits=3)
course_23 = Course(id=23, serial='CSC 48000', name='Computer Security', dept='CSC', description='Understand the fundamentals of perfect security and cryptography', designation="Group A Elective", credits=3)
course_24 = Course(id=24, serial='CSC 48600', name='Computational Complexity', dept='CSC', description='Computational feasability v.s NP Completeness', designation="Group A Elective", credits=3)
course_25 = Course(id=25, serial='CSC 44000', name='Computational Methods', dept='CSC', description='Learn the methods to efficiently solve numerical issues', designation="Group B Elective", credits=3)
course_26 = Course(id=26, serial='CSC 44200', name='Systems Simulation', dept='CSC', description='How to implement Dynamic system simulations', designation="Group B Elective", credits=3)
course_27 = Course(id=27, serial='CSC 44600', name='Math Optimization Tech', dept='CSC', description='Learn optimal methods for solving complex mathematics', designation="Group B Elective", credits=3)
course_28 = Course(id=28, serial='CSC 47000', name='Image Processing', dept='CSC', description='Learn image processing/enhancement', designation="Group B Elective", credits=3)
course_29 = Course(id=29, serial='CSC 47100', name='Computer Vision', dept='CSC', description='Utilize Neural Networks and deep learning to create visualization models', designation="Group B Elective", credits=3)
course_30 = Course(id=30, serial='CSC 47200', name='Computer Graphics', dept='CSC', description='Use C++, Qt and modern OpenGL to make computer generated images', designation="Group B Elective", credits=3)
course_31 = Course(id=31, serial='CSC 47900', name='Digital Libraries', dept='CSC', description='Learn to make and take advantage of exisiting digital libraries', designation="Group B Elective", credits=3)
course_32 = Course(id=32, serial='CSC 31800', name='Internet Programming', dept='CSC', description='Learn network protocols, and lossless data transmission algorithms', designation="Group C Elective", credits=3)
course_33 = Course(id=33, serial='CSC 41200', name='Computer Networks', dept='CSC', description='Understanding the physical layers of network transmission', designation="Group C Elective", credits=3)
course_34 = Course(id=34, serial='CSC 42000', name='Compiler Construction', dept='CSC', description='Use Pushdown Automatons to traverse Context Free grammar compilers', designation="Group C Elective", credits=3)
course_35 = Course(id=35, serial='CSC 43000', name='Distributed Computing', dept='CSC', description='Learn the fundamentals of a distributed system', designation="Group C Elective", credits=3)
course_36 = Course(id=36, serial='CSC 43500', name='Concurrency in Operating Systems', dept='CSC', description='Intermediate Unix Operating Systems course', designation="Group C Elective", credits=3)
course_37 = Course(id=37, serial='CSC 43800', name='Real-Time Computing Systems', dept='CSC', description='Understanding the fundamentals of real time computing systems', designation="Group C Elective", credits=3)
course_38 = Course(id=38, serial='CSC 47300', name='Website and Web Applications', dept='CSC', description='Full Stack development course in AGILE', designation="Group C Elective", credits=3)


CS_courses = [course_1, course_2, course_3, course_4, course_5, course_6, course_7, course_8, course_9, course_10, course_11, course_12, course_13, course_14, course_15, course_16, course_17, course_18, course_19, course_20, course_21, course_22, course_23, course_24, course_25, course_26, course_27, course_28, course_29, course_30, course_31, course_32, course_33, course_34, course_35, course_36, course_37, course_38]
db.session.add_all(CS_courses)


# -- Mathematics:

course_39 = Course(id=39, serial='MATH 20100', name='Calculus I', dept='MATH', description='Understanding relations, variance, and derivatives', designation="Core Requirement", credits=3)
course_40 = Course(id=40, serial='MATH 20200', name='Calculus II', dept='MATH', description='L hospitals Rule, integrals', designation="Core Requirement", credits=3)
course_41 = Course(id=41, serial='MATH 20300', name='Calculus III', dept='MATH', description='3 dimensional relations, and integrals', designation="Core Requirement", credits=4)
course_42 = Course(id=42, serial='MATH 34600', name='Elements of Linear Algebra', dept='MATH', description='Matrix mathematics', designation="Core Requirement", credits=3)


db.session.add(course_39)
db.session.add(course_40)
db.session.add(course_41)
db.session.add(course_42)


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


# -- Required Liberal Art Courses: 

course_49 = Course(id=49, serial='ENGL 11000', name='Freshman Composition', dept='ENGL', description='Fundamental English reading, writing, comprehention', designation="Required Liberal Art", credits=3)
course_50 = Course(id=50, serial='SPEECH 11100', name='Foundations of Speech Communication', dept='THEATRE/SPEECH', description='Apply public speaking skills', designation="Required Liberal Art", credits=3)
course_51 = Course(id=51, serial='ENGL 21007', name='Writing for Engineering', dept='ENGL', description='Learn to write Scientific and scholarly articles on engineering', designation="Required Liberal Art", credits=3)
course_52 = Course(id=52, serial='ECO 10400', name='Intro to Quantitative Economics', dept='ECO', description='Learning market fundamentals of supply and demand.', designation="Required Liberal Art", credits=3)
course_53 = Course(id=53, serial='ENGR 27600', name='Engineering Economics', dept='ENGR', description='Learning fundamentals engineering economics', designation="Required Liberal Art", credits=3)

db.session.add(course_49)
db.session.add(course_50)
db.session.add(course_51)
db.session.add(course_52)
db.session.add(course_53)


# --   (Pathways) Liberal Art courses: [CE = Creative Expression (1000 level)] ( NOTE: This does not include EVERY possible option in CCNY)

course_54 = Course(id=54, serial='ART 10000', name='Intro to the world of Art', dept='ART', description='Learn the history of modern art', designation="[CE](1000)", credits=3)
course_55 = Course(id=55, serial='MUS 10100', name='Introduction to Music', dept='MUS', description='Fundamentals of Music Theory', designation="[CE](1000)", credits=3)
course_56 = Course(id=56, serial='MUS 10200', name='Introduction to World Music', dept='MUS', description='Learn the history of music', designation="[CE](1000)", credits=3)
course_57 = Course(id=57, serial='THTR 13100', name='Introduction to Theatre', dept='THEATRE/SPEECH', description='Learn the basics of theatrical productions', designation="[CE](1000)", credits=3)

db.session.add(course_54)
db.session.add(course_55)
db.session.add(course_56)
db.session.add(course_57)


# --   (Pathways) Liberal Art courses: [WCGI = World Cultures and Global Issues (1000 level)] ( NOTE: This does not include EVERY possible option in CCNY)
course_58 = Course(id=58, serial='JWST 11700', name='The Bible as Literature', dept='JWST', description='Learn the history of bible literature', designation="[WCGI](1000)", credits=3)
course_59 = Course(id=59, serial='WHUM 10100', name='World Humanities I', dept='ART', description='The foundation of world humanities', designation="[WCGI](1000)", credits=3)
course_60 = Course(id=60, serial='WHUM 10200', name='World Humanities II', dept='ART', description='Intermediate world humanities principles', designation="[WCGI](1000)", credits=3)
course_61 = Course(id=61, serial='ANTH 10100', name='General Anthropology', dept='ANTH', description='Introduction to the field of anthropology', designation="[WCGI](1000)", credits=3)
course_62 = Course(id=62, serial='ASIA 10100', name='Asia and it\'s people', dept='ASIA', description='Learn about the people from largest, most diverse continent on earth', designation="[WCGI](1000)", credits=3)
course_63 = Course(id=63, serial='BLST 10200', name='African Heritage: Caribbean-Brazilian Experience', dept='BLST', description='Learn the history of black heritage in the Carribean/Brazil', designation="[WCGI](1000)", credits=3)
course_64 = Course(id=64, serial='WCIV 10100', name='World Civilizations I: Prehistory to 1500 AD', dept='HIST', description='Patheolic Era, to the Roman Empire', designation="[WCGI](1000)", credits=3)
course_65 = Course(id=65, serial='WCIV 10200', name='World Civilizations II: 1500 AD to present', dept='HIST', description='Early Roman Empire to modern age', designation="[WCGI](1000)", credits=3)

db.session.add(course_58)
db.session.add(course_59)
db.session.add(course_60)
db.session.add(course_61)
db.session.add(course_62)
db.session.add(course_63)
db.session.add(course_64)
db.session.add(course_65)


# --   (Pathways) Liberal Art courses: [IS = Individual and Society (1000 level)] ( NOTE: This does not include EVERY possible option in CCNY)
course_66 = Course(id=66, serial='ECO 10250', name='Principles of Microeconomics', dept='ECO', description='Learn economics on a Micro scale', designation="[IS](1000)", credits=3)
course_67 = Course(id=67, serial='LIB 10000', name='Research in the Digital Age: Media & Information Literacy', dept='LIB', description='Learn about information on media techniques', designation="[IS](1000)", credits=3)
course_68 = Course(id=68, serial='PSY 10200', name='Psychology in Modern World', dept='PSY', description='Understand the evolution of modern pschyology', designation="[IS](1000)", credits=3)
course_69 = Course(id=69, serial='SOC 10500', name='Individual, Group and Society', dept='SOC', description='An Introduction to Sociology', designation="[IS](1000)", credits=3)
course_70 = Course(id=70, serial='WS 10000', name='Women’s/Gender Roles in Contemporary Society', dept='WS', description='An evaluation of the society and gender roles', designation="[IS](1000)", credits=3)

db.session.add(course_66)
db.session.add(course_67)
db.session.add(course_68)
db.session.add(course_69)
db.session.add(course_70)


# --   (Pathways) Liberal Art courses: [US = US Experience in its Diversity (1000 level)] ( NOTE: This does not include EVERY possible option in CCNY)
course_71 = Course(id=71, serial='PSC 10100', name='American Government and Politics', dept='PSC', description='Our politics go back to our founding fathers', designation="[US](1000)", credits=3)
course_72 = Course(id=72, serial='USSO 10100', name='US Society', dept='USSO', description='The history of the US', designation="[US](1000)", credits=3)
course_73 = Course(id=73, serial='BLST 10100', name='African Heritage and the Afro-American Experience', dept='BLST', description='Afro-American Experience in America', designation="[US](1000)", credits=3)
course_74 = Course(id=74, serial='PHIL 10200', name='Intro to Philosophy', dept='PHIL', description='Logical Reasoning, Descartes Enlightment Era', designation="[US](1000)", credits=3)

db.session.add(course_71)
db.session.add(course_72)
db.session.add(course_73)
db.session.add(course_74)


# --   (Pathways) Liberal Art courses: [CE = Creative Expression (2000 level)] ( NOTE: This does not include EVERY possible option in CCNY)

course_75 = Course(id=75, serial='AES 23202', name='Survey of World Architecture I', dept='AES', description='Arch. & Env. Studies', designation="[CE](2000)", credits=3)
course_76 = Course(id=76, serial='AES 24202', name='Survey of World Architecture II', dept='AES', description='Arch. & Env. Studies', designation="[CE](2000)", credits=3)
course_77 = Course(id=77, serial='URB 20010', name='Introduction to Urban Studies', dept='URB', description='Urban Studies', designation="[CE](2000)", credits=3)

db.session.add(course_75)
db.session.add(course_76)
db.session.add(course_77)


# --   (Pathways) Liberal Art courses: [WCGI = World Cultures and Global Issues (2000 level)] ( NOTE: This does not include EVERY possible option in CCNY)
course_78 = Course(id=78, serial='ANTH 20000', name='Archaeology', dept='ANTH', description='Study of humans NOT Dinosaurs!', designation="[WCGI](2000)", credits=3)
course_79 = Course(id=79, serial='ASIA 20200', name='Contemporary Asia', dept='ASIA', description='Learn about Asian Culture and history', designation="[WCGI](2000)", credits=3)
course_80 = Course(id=80, serial='ASIA 20500', name='Contemporary China', dept='ASIA', description='History of Chinese Dynasties', designation="[WCGI](2000)", credits=3)
course_81 = Course(id=81, serial='FREN 28300', name='The Literature of Contemporary France', dept='FREN', description='The evolution of french literature', designation="[WCGI](2000)", credits=3)
course_82 = Course(id=82, serial='HIST 20400', name='Early Modern Europe', dept='HIST', description='Fall of Rome, Rennaisance', designation="[WCGI](2000)", credits=3)
course_83 = Course(id=83, serial='HIST 20600', name='Modern Europe', dept='HIST', description='Barouqe era, WW2, present', designation="[WCGI](2000)", credits=3)
course_84 = Course(id=84, serial='HIST 23700', name='Asia and the World', dept='HIST', description='Asian history and development', designation="[WCGI](2000)", credits=3)
course_85 = Course(id=85, serial='HIST 23800', name='The Middle East in Global History', dept='HIST', description='History of ancient middle eastern societies', designation="[WCGI](2000)", credits=3)
course_86 = Course(id=86, serial='HIST 27600', name='Africa and the Modern World', dept='HIST', description='African influence in the modern world', designation="[WCGI](2000)", credits=3)
course_87 = Course(id=87, serial='INTL 20100', name='International Studies: A Global Perspective', dept='INTL', description='Global Geo political history', designation="[WCGI](2000)", credits=3)
course_88 = Course(id=88, serial='SPAN 28100', name='Masterworks of Spanish Literature I', dept='SPAN', description='Spanish Literature I', designation="[WCGI](2000)", credits=3)
course_89 = Course(id=89, serial='SPAN 28300', name='Masterworks of Latin American Literature', dept='SPAN', description='Spanish Literature from Latin America', designation="[WCGI](2000)", credits=3)
course_90 = Course(id=90, serial='THTR 21100', name='Theatre History 1', dept='THEATRE/SPEECH', description='From ancient greece to William Shakespeare learn the history of theatre', designation="[WCGI](2000)", credits=3)
course_91 = Course(id=91, serial='THTR 21200', name='Theatre History 2', dept='THEATRE/SPEECH', description='Middle Age Theatre', designation="[WCGI](2000)", credits=3)
course_92 = Course(id=92, serial='THTR 21300', name='Theatre History 3', dept='THEATRE/SPEECH', description='Broadway and Modern Theatre', designation="[WCGI](2000)", credits=3)


WCGI_2000 = [course_78, course_79, course_80, course_81, course_82, course_83, course_84, course_85, course_86, course_87, course_88, course_89, course_90, course_91, course_92]
db.session.add_all(WCGI_2000)

# --   (Pathways) Liberal Art courses: [IS = Individual and Society (2000 level)] ( NOTE: This does not include EVERY possible option in CCNY)
course_93 = Course(id=93, serial='ANTH 20100', name='Cross Cultural Perspectives', dept='ANTH', description='Learn about different social norms and perspectives', designation="[IS](2000)", credits=3)
course_94 = Course(id=94, serial='EDCE 25600', name='Language, Mind, and Society', dept='EDCE', description='Varies by instructor', designation="[IS](2000)", credits=3)
course_95 = Course(id=95, serial='JWST 28100', name='The Holocaust', dept='JWST', description='Experience survivor stories of the past, and reflect on what you would do. You don\'t need to answer. All questions are rhetorical!', designation="[IS](2000)", credits=3)


db.session.add(course_93)
db.session.add(course_94)
db.session.add(course_95)


# --   (Pathways) Liberal Art courses: [US = U.S. Experince in its Diversity (2000 level)] (NOTE: This does not include EVERY possible option in CCNY)
course_96 = Course(id=96, serial='HIST 24000', name='The United States: From Its Origins to 1877', dept='HIST', description='Colonial Era to 1877', designation="[US](2000)", credits=3)
course_97 = Course(id=97, serial='HIST 24100', name='The United States since 1865', dept='HIST', description='The aftermath of the Civil war, reconstruction, jim crow, WW2, Civil Rights Movement, Cold War, to present', designation="[US](2000)", credits=3)

db.session.add(course_96)
db.session.add(course_97)


# -- Technical Elective Options (Miscellanious) (NOTE: This does not include EVERY possible option in CCNY)

course_98 = Course(id=98, serial='EAS 21700', name='Systems Analysis of the Earth', dept='EAS', description='Analysis and modeling of plate tectonics and climate change', designation="Technical Elective", credits=4)
course_99 = Course(id=99, serial='EAS 22700', name='Structural Geology', dept='EAS', description='Geometry of elementary earth structures', designation="Technical Elective", credits=4)
course_100 = Course(id=100, serial='EAS 30800', name='ESS Modeling/ Databases', dept='EAS', description='Modeling of global and local environmental problems', designation="Technical Elective", credits=3)
course_101 = Course(id=101, serial='PHY 20300', name='General Physics I', dept='PHY', description='Introductory Physics for life science majors and pre-med/bio majors', designation="Technical Elective", credits=4)
course_102 = Course(id=102, serial='PHY 20400', name='General Physics II', dept='PHY', description='Intermediate Physics for life science majors and pre-med/bio majors', designation="Technical Elective", credits=4)
course_103 = Course(id=103, serial='PHYS 20900', name='University Physics III', dept='PHY', description='Calculus-based study of the basic concepts of wave motion, physical optics, and modern physics.', designation="Technical Elective", credits=4)
course_104 = Course(id=104, serial='MATH 20500', name='Elements of Calculus', dept='MATH', description='Introduction to calculus for life science majors and pre-med/bio majors', designation="Technical Elective", credits=3)
course_105 = Course(id=105, serial='MATH 21200', name='Calculus II with Introduction to Multivariable Functions', dept='MATH', description='Techniques of integration, improper integrals, infinite sequences and series, parametric equations, etc', designation="Technical Elective", credits=3)
course_106 = Course(id=106, serial='MATH 21300', name='Calculus III with Vector Analysis', dept='MATH', description='Applications of partial differentiation, vector-valued functions, multiple integrals, vector fields, line integrals, and theorems of Green, Stokes, and Gauss.', designation="Technical Elective", credits=3)
course_107 = Course(id=107, serial='MATH 39100', name='Methods of Differential Equations', dept='MATH', description='First order equations; higher order linear equations with constant coefficients, undetermined coefficients, variation of parameters, applications; Euler\'s equation.', designation="Technical Elective", credits=3)
course_108 = Course(id=108, serial='MATH 39104', name='Methods of Differential Equations', dept='MATH', description='This course omits a few topics,e.g. Laplace transforms, in order to supplement the solution methods of Math 391 with some theoretical background, especially links with linear algebra.', designation="Technical Elective", credits=3)
course_109 = Course(id=109, serial='MATH 39200', name='Linear Algebra and Vector Analysis for Engineers', dept='MATH', description='Matrix theory, linear equations, Gauss elimination, determinants, eigenvalue problems', designation="Technical Elective", credits=3)
course_110 = Course(id=110, serial='MATH 39204', name='Linear Algebra and Vector Analysis for Engineers', dept='MATH', description='Matrix theory, linear equations, Gauss elimination, determinants, general vector spaces, basis and dimension,vector feild theory', designation="Technical Elective", credits=3)
course_111 = Course(id=111, serial='CHEM 21000', name='Applied Chemistry For Biomedical Engineers', dept='CHEM', description='Intro to basic organic chemistry and how it relates to the human body', designation="Technical Elective", credits=4)
course_112 = Course(id=112, serial='CHEM 24300', name='Quantitative Analysis', dept='CHEM', description='Volumetric, spectrophotometric and electrometric analyses.', designation="Technical Elective", credits=4)
course_113 = Course(id=113, serial='CHEM 26100', name='Organic Chemistry I', dept='CHEM', description='The Course that makes all pre-med students cry!', designation="Technical Elective", credits=3)
course_114 = Course(id=114, serial='BIO 20600', name='Introduction to Genetics', dept='BIO', description='DNA organization, chromosome structure, genes and alleles, etc', designation="Technical Elective", credits=4)
course_115 = Course(id=115, serial='BIO 20700', name='Organismic Biology', dept='BIO', description='This course emphasizes the physiological adjustments organisms make to specific challenges in their environments', designation="Technical Elective", credits=4)
course_116 = Course(id=116, serial='BIO 22800', name='Ecology and Evolution', dept='BIO', description='Introduction to the basic principles of ecology and evolutionary biology emphasizing quantitative approaches and hypothesis testing.', designation="Technical Elective", credits=4)
course_117 = Course(id=117, serial='BIO 31100', name='Selected Topics In Biology', dept='BIO', description='Discussions, student seminars, literature survey, varies by instructor', designation="Technical Elective", credits=4)
course_118 = Course(id=118, serial='BIO 32100', name='Physiological Processes', dept='BIO', description='This course is designed to introduce fundamental concepts of physiology to biomedical engineering students.', designation="Technical Elective", credits=4)
course_119 = Course(id=119, serial='BIO 33000', name='Survey Of The Vertebrates', dept='BIO', description='Survey of the major features of the vertebrates, including brief modern classification of the major groups', designation="Technical Elective", credits=3)
course_120 = Course(id=120, serial='BIO 34000', name='Biology Of Invertebrates', dept='BIO', description='The structure and function of various invertebrates selected to illustrate morphological, physiological and ecological adaptations.', designation="Technical Elective", credits=4)
course_121 = Course(id=121, serial='ENGR 20400', name='Electrical Circuits', dept='ENGR', description='Intermediate circuits course', designation="Technical Elective", credits=3)
course_122 = Course(id=122, serial='ENGR 23000', name='Thermodynamics', dept='ENGR', description='Introductory concepts and definitions. Zeroth Law and absolute temperature. Work and Heat, etc', designation="Technical Elective", credits=3)
course_123 = Course(id=123, serial='ENGR 30000', name='Social, Economic And Cultural Impact Of Biomedical Technology', dept='ENGR', description='varies by instructor', designation="Technical Elective", credits=3)
course_124 = Course(id=124, serial='ENGR 41230', name='The Management Of Hazardous Wastes', dept='ENGR', description='The course introduces the regulatory framework and science fundamentals for the management of hazardous wastes.', designation="Technical Elective", credits=3)

course_125 = Course(id=125, serial='INDP XX001', name='Independent Study I', dept='Arbitrary', description='Varies by Instructor (departmental consent required)', designation="Technical Elective", credits=3)
course_126 = Course(id=126, serial='INDP XX002', name='Independent Study II', dept='Arbitrary', description='Varies by Instructor (departmental consent required)', designation="Technical Elective", credits=3)


Technical_Electives = [course_98, course_99, course_100, course_101, course_102, course_103, course_104, course_105, course_106, course_107, course_108, course_109, course_110, course_111, course_112, course_113, course_114, course_115, course_116, course_117, course_118, course_119, course_120, course_121, course_122, course_123, course_124, course_125, course_126]
db.session.add_all(Technical_Electives)


"""
# -- For anyone wondering this was the GSoE Flexible Core list I used: 
# -- https://www.ccny.cuny.edu/engineering/flexible-core
"""


# -- Grade Options:
grade_1 = Grade(id=1, value='')
grade_2 = Grade(id=2, value='IP')
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
# grade_15 = Grade(id=15, value='T')      # This is for Transfer Students!!! I'm not sure if this will break anything, so I'll comment this out for now. Focus on one thing at a time! 

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


# -- EditWorkflow options:

editworkflow = Editworkflow()
db.session.add(editworkflow) 




db.session.commit()     # One single commit is much more efficient! 



#-----------------------------------------------------------------

"""
# Only use this file by running: 

#------------------------------------
#     $ python clean_up.py
#------------------------------------

# This will re-create the DB file. And initialize the Database with some starting data! 
# Make sure to run this every time any changes are made
# To models.py, before you plan to execute run.py 

"""

#-----------------------------------------------------------------