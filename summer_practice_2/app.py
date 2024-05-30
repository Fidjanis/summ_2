from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Client, Service, Employee, CashJournal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/serv')
def service():
    servs = Service.query.all()
    return render_template('serv.html',servs=servs)

@app.route('/emp')
def employee():
    emps=Employee.query.all()
    return render_template('emp.html',emps=emps)

@app.route('/cl')
def client():
    cls=Client.query.all()
    return render_template('cl.html',cls=cls)

@app.route('/cj')
def cash_journal():
    cjs=CashJournal.query.all()
    return render_template('cj.html',cjs=cjs)

@app.route('/addserv', methods=['GET', 'POST'])
def add_serv():
    if request.method == 'POST':
        name = request.form['name']
        rate = request.form['rate']
        serv = Service(name=name, rate=rate)
        db.session.add(serv)
        db.session.commit()
        return redirect('/')
    return render_template('addserv.html')

@app.route('/addemp', methods=['GET', 'POST'])
def add_emp():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        job = request.form['job']
        emp = Employee(name=name, age=age, job=job)
        db.session.add(emp)
        db.session.commit()
        return redirect('/emp')
    return render_template('addemp.html')

@app.route('/addcl', methods=['GET', 'POST'])
def add_cl():
    if request.method == 'POST':
        value = request.form['value']
        fromName = request.form['fromName']
        toName = request.form['toName']
        cl = Client(value=value,fromName=fromName,toName=toName)
        db.session.add(cl)
        db.session.commit()
        return redirect('/cl')
    return render_template('addcl.html')

@app.route('/addcj', methods=['GET', 'POST'])
def add_cj():
    if request.method == 'POST':
        data = request.form['data']
        cost = request.form['cost']
        ser = request.form['ser']
        cj = CashJournal(data=data,cost=cost,ser=ser)
        db.session.add(cj)
        db.session.commit()
        return redirect('/cj')
    return render_template('addcj.html')

@app.route('/editserv/<int:id>', methods=['GET', 'POST'])
def edit_serv(id):
    serv = Service.query.get_or_404(id)
    if request.method == 'POST':
        serv.name = request.form['name']
        serv.rate = request.form['rate']
        db.session.commit()
        return redirect('/serv')
    return render_template('editserv.html', serv=serv)

@app.route('/editemp/<int:id>', methods=['GET', 'POST'])
def edit_emp(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.age = request.form['age']
        emp.job = request.form['job']
        db.session.commit()
        return redirect('/emp')
    return render_template('editemp.html', emp=emp)

@app.route('/editcl/<int:id>', methods=['GET', 'POST'])
def edit_cl(id):
    cl = Client.query.get_or_404(id)
    if request.method == 'POST':
        cl.value = request.form['value']
        cl.fromName = request.form['fromName']
        cl.toName = request.form['toName']
        db.session.commit()
        return redirect('/cl')
    return render_template('editcl.html', cl=cl)

@app.route('/editcj/<int:id>', methods=['GET', 'POST'])
def edit_cj(id):
    cj = CashJournal.query.get_or_404(id)
    if request.method == 'POST':
        cj.value = request.form['data']
        cj.fromName = request.form['cost']
        cj.toName = request.form['ser']
        db.session.commit()
        return redirect('/cj')
    return render_template('editcj.html', cj=cj)



@app.route('/delete_serv/<int:id>', methods=['POST'])
def delete_serv(id):
    serv = Service.query.get_or_404(id)
    db.session.delete(serv)
    db.session.commit()
    return redirect('/serv')

@app.route('/delete_cl/<int:id>', methods=['POST'])
def delete_cl(id):
    cl = Client.query.get_or_404(id)
    db.session.delete(cl)
    db.session.commit()
    return redirect('/cl')

@app.route('/delete_emp/<int:id>', methods=['POST'])
def delete_emp(id):
    emp= Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect('/emp')

@app.route('/delete_cj/<int:id>', methods=['POST'])
def delete_cj(id):
    cj = CashJournal.query.get_or_404(id)
    db.session.delete(cj)
    db.session.commit()
    return redirect('/cj')

if __name__ == '__main__':
    app.run(debug=True)