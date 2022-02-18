from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninjas():
    dojo = Dojo.get_all()
    return render_template('add_ninja.html', dojo=dojo)

@app.route('/create_ninja', methods=["POST"])
def create_ninjas():
    Ninja.save_ninja(request.form)
    return redirect('/dojos')