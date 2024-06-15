from flask import Flask, url_for, request, render_template
from .views import *

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page."


@app.route("/hello")
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template("hello.html", person=name)


@app.route('/login')
def old_login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_login_form()
    

@app.get('/login')
def login_get():
    return show_login_form()

@app.post('/login')
def login_post():
    return do_the_login()


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Depp'))