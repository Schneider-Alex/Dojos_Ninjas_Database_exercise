from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template("index.html", all_dojos = Dojo.get_all())

@app.route('/create_dojo', methods=["POST"])
def createdojo():
    data = {
        'name' : request.form["name"]
    }
    Dojo.save(data)
    return  redirect('/')

@app.route('/dojoninjas/<int:dojo_id>')
def see_dojo_ninjas(dojo_id):
    data = {
        'id' : dojo_id
    }
    return render_template('displaydojo.html', specificdojo=Dojo.get_dojo_with_ninjas(data))

