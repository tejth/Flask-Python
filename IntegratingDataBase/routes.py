from models import Person
from flask import render_template, request, redirect, url_for

def register_routes(app, db):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':  
            people = Person.query.all()
            return render_template('index.html', people=people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age = request.form.get('age')
            job = request.form.get('job')
            
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()
            
            return redirect(url_for('index'))
          
    @app.route('/delete/<int:pid>', methods=['POST'])
    def delete(pid):
        person = Person.query.get(pid)
        if person:
            db.session.delete(person)
            db.session.commit()
        return redirect(url_for('index'))
    
    @app.route('/details/<int:pid>')
    def details(pid):
        person = Person.query.get(pid)
        return render_template('details.html', person=person)
