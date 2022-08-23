from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def new_table():
    db.create_all()
