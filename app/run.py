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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')      # displays success message in bootstrap green! 
        return redirect(url_for('home'))                                    # redirects us to the home page! 
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)