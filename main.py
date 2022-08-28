from flask import Flask
from extension import db
from routes import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
user='root', password='', server='localhost', database='Evento')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(main)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)