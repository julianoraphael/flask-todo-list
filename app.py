from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
    with app.app_context():
        tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    new_task = Task(task=task)
    with app.app_context():
        db.session.add(new_task)
        db.session.commit()
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    task_id = request.form.get('task_id')
    with app.app_context():
        task = Task.query.get(int(task_id))  # Cast task_id to integer
        if task:
            db.session.delete(task)
            db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
