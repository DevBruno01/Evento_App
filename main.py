from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', password='', server='localhost', database='Evento')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    local = db.Column(db.String(100))
    data = db.Column(db.String(100))
    hour = db.Column(db.String(100))

    def __init__(self, name, local, data, hour):
        self.name = name
        self.local = local
        self.data = data
        self.hour = hour


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results')
def render_results():
    return render_template("results.html")


@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    local = request.form['local']
    date = request.form['date']
    hour = request.form['hour']

    my_data = Data(name, local, date, hour)
    db.session.add(my_data)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
