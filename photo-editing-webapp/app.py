from flask import Flask, render_template

app = Flask(__name__)

Posts = [
    {
        'author':'Corey Shafer',
        'title': 'Blog Post 1',
        'content':'food',
        'date_posted':'Nov 18, 2023'
    },
    {
        'author':'Shawty ',
        'title': 'Blog Post 2',
        'content':'art',
        'date_posted':'Nov 18, 2023'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=Posts)


@app.route("/about")
def about():
    return render_template('about.html')