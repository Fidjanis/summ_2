from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    #__tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Float, nullable=False)
    job = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Employee(name='{self.name}', age='{self.age}', job='{self.job}')"


class Service(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Service(name='{self.name}', rate='{self.rate}')"


class Client(db.Model):
    #__tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(250), nullable=False)
    fromName = db.Column(db.String(250), nullable=False)
    toName = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Operation(Value: '{self.value}', from: '{self.fromName}', to: {self.toName})"


class CashJournal(db.Model):
    #__tablename__ = 'cash_journal'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(250), nullable=False)
    cost = db.Column(db.String(250), nullable=False)
    ser = db.Column(db.String(250), nullable=False)
    #client_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    #employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)

    #client = db.relationship("Client")
    #employee = db.relationship("Employee")

    def __repr__(self):
        return f"CashJournal(Date: '{self.data}', Cost: '{self.cost}', Service: {self.ser})"

