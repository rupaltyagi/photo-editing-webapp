from flask import Flask, render_template, request, send_from_directory, url_for
from forms import RegistrationForm, LoginForm
from flask_uploads import UploadSet, IMAGES, configure_uploads
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'andsknfjkds'
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder 

#photos = UploadSet('photos', IMAGES)

#configure_uploads(app, photos)
app.debug=True


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
@app.route("/upload", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('home.html', img=img)
    return render_template('home.html')


# @app.route("/upload", methods=['POST', 'GET'])
# def display_file():
#   return render_template('home.html', img=img)
#   return send_from_directory(app.config['UPLOAD'], img)



@app.route("/about")
def about():
    return render_template('about.html')


# @app.route("/register")
# def register():
#     form = RegistrationForm()
#     return render_template('register.html')
    

@app.route("/login")
def login():
    # form = LoginForm()
    return render_template('login.html')
