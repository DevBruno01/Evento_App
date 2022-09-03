from flask import Blueprint, redirect, render_template, request, url_for, flash
from extension import db
from models import Data
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField

main = Blueprint('main', __name__)

class EventoForm(FlaskForm):
    Nome_Evento = StringField('Nome_Evento')
    Local = StringField('Local')
    Data_do_Evento = DateField('Data_do_Evento', format='%Y-%m-%d')
    Hora_do_Evento = TimeField('Hora_do_Evento', format='%H:%M')

@main.route('/')
def index():
    form = EventoForm()
    return render_template("index.html", form=form)


@main.route('/results')
def render_results():
    all_data = Data.query.all()
    return render_template("results.html", evento=all_data)


@main.route('/insert', methods=['GET','POST'])
def insert():
    form = EventoForm()

    if form.validate_on_submit():
        my_data = Data(form.Nome_Evento.data, form.Local.data, form.Data_do_Evento.data, form.Hora_do_Evento.data)
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