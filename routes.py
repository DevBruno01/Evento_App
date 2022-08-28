from flask import Blueprint, redirect, render_template, request, url_for
from extension import db
from models import Data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/results')
def render_results():
    all_data = Data.query.all()
    return render_template("results.html", evento=all_data)


@main.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        local = request.form['local']
        date = request.form['date']
        hour = request.form['hour']

        my_data = Data(name, local, date, hour)
        db.session.add(my_data)
        db.session.commit()

    return redirect(url_for('main.index'))