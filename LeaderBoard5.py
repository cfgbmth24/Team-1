from flask import Flask, render_template, redirect, url_for,request
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 

import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'

db = SQLAlchemy(app)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
    form = Register_Form()
    if request.method == 'POST':
        new_user = User(username=form.username.data)
        db.session.add(new_user)
        
        db.session.commit()
        print("commit")

        return redirect(url_for('series'))
    return render_template('loginPage.html', form=form)

@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('sportSeriesPage.html')

@app.route('/series', methods=['GET', 'POST'])
def series():
    return render_template('userSeriesPage.html')

@app.route('/points', methods=['GET', 'POST'])
def profile():
    return render_template('pointsHistoryPage.html')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    score = db.Column(db.Integer)
class Register_Form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    submit = SubmitField("Register")

    def check_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists ")

if __name__ == '__main__':
    if not os.path.exists('Leaderboard.db'):
        db.create_all()
    app.run(debug=True)