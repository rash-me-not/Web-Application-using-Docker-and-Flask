from flask import Flask,render_template,request,url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
from models import Players,db
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
db_uri = 'mysql://agsroot:ags@db:3306/aztecgames'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/") 
def index():
    return render_template("index.html")
   
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    release_date  = datetime(2018,12,1).date()
    date = datetime.now().date()
    difference = release_date - date
    return render_template("game_release.html",Message = "{} days for the next Game Release".format(difference.days), Release_date = release_date, )

@app.route("/login", methods=['POST', 'GET'])
def login():
    error =None
    if request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
        if user is not None :
            player = Players.query.filter(Players.username == user).first()
        if player.password == passw:
            session['username'] = user
            currentTime = datetime.now()
            return render_template("welcome.html", username = session['username'], current_login_time = currentTime)
        else:
            session['username'] = None
            flash("Invalid username/password")
            return redirect(url_for('index'))
            

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/registerAction", methods=['POST'])
def registerAction():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        dob = request.form['dob']
        phone = request.form['phone']
        phone_type = request.form.get('phone_type')
        fav_game = request.form['fav_game']
        user = Players(first_name, last_name, username, password, dob, phone,phone_type,fav_game)
        db.session.add(user)
        db.session.commit()
        session['username'] = username
    currentTime = datetime.now()
    return render_template("welcome.html", username = session['username'], current_login_time = currentTime)
      
    

    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')