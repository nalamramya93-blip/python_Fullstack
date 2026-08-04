from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session

# serve templates from project root (existing HTML files) and static files from /static
app = Flask(__name__, template_folder='.', static_folder='static', static_url_path='/static')
app.secret_key = 'dev'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/trainers')
def trainers():
    return render_template('trainers.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    