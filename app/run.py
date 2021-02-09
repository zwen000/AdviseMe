from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '3a005a74e33b93ce317f78c78fb2577d'


posts = [
    {
        'author': 'Rehman Arshad',
        'title': 'Hello World',
        'content': 'First post content',
        'date_posted': 'April 20th, 2020'
    }, 
    {
        'author': 'Dante',
        'title': 'DMC 3 se',
        'content': 'Jackpot!',
        'date_posted': 'April 20th, 2006'
    },
    {
        'author': 'Vergil',
        'title': 'DMC 3 se',
        'content': 'Wheres your motivation?',
        'date_posted': 'April 20th, 2006'
    }
]

# Ignore the text above that is just dummy data ... 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


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