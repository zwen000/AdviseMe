from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '3a005a74e33b93ce317f78c78fb2577d'



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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()                                                                   # create the form
    if form.validate_on_submit():                                                               # if our form is valid on submission (i.e there are no errors)
        flash(f'Account created for {form.username.data}!', 'success')                          # display success message in bootstrap green!
        return redirect(url_for('home'))                                                        # redirects user to the home page!
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                                                          # create the form
    if form.validate_on_submit():                                                               # if our form is valid on submission (i.e there are no errors)
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':            # if this checks pass
            flash('You have been logged in!', 'success')                                        # display success message in bootstrap green!
            return redirect(url_for('home'))                                                    # redirect user to the home page!
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')      # display success message in bootstrap red!
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)
