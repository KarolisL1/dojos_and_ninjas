from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    dojo = Dojo.get_all()
    return render_template('index.html', dojo=dojo)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def single_dojo(dojo_id):
    data = {'dojo_id': dojo_id}
    dojo = Dojo.get_one_dojo(data)
    return render_template('dojo_show.html', dojo=dojo)