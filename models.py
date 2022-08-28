from extension import db, new_table

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    local = db.Column(db.String(100))
    date = db.Column(db.String(100))
    hour = db.Column(db.String(100))


    def __init__(self, name, local, date, hour):
        self.name = name
        self.local = local
        self.date = date
        self.hour = hour
        new_table()


