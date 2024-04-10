from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.Integer)
class Register_Form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    submit = SubmitField("Register")


@app.route('/')
def index():
    #form = Register_Form()
   # if form.validate_on_submit():
        #new_user = User(username=form.username.data)
        #db.session.add(new_user)
        #db.session.commit()
        #return redirect(url_for('series'))
    return render_template('index10.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/series')
def series():
    return render_template('series.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    if not os.path.exists('Leaderboard.db'):
        db.create_all()
    app.run(debug=True)