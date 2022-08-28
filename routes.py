from flask import Blueprint, redirect, render_template, request, url_for, flash
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
        flash("Employee inserted Successfully")

    return redirect(url_for('main.index'))

@main.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('main.render_results'))

@main.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.local = request.form['local']
        my_data.date = request.form['date']
        my_data.hour = request.form['hour']
        db.session.commit()
        flash("Employee Updated Successfuly")

        return redirect(url_for('main.render_results'))