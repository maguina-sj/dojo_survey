from flask_app import app
from flask_app.models.dojo import Dojo
from flask import Flask, render_template, session, request, redirect, flash

@app.route('/')
def index ():
    return render_template('index.html')

# @app.route('/process/', methods=['POST'])
# def process ():
#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comment'] = request.form['comments']
#     return redirect('/result/')


@app.route('/result/')
def result():
    lastdojo = Dojo.getLastOne()
    return render_template('result.html', lastdojo=lastdojo)

@app.route('/create/', methods=['POST'])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect ('/result/')