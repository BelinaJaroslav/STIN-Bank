from flask import Flask, render_template, request, redirect, url_for, session, make_response
import requests

import datetime
import random
import string
import smtplib
import json

app = Flask(__name__)

sender = "stintest@outlook.com"
pw = "Burnerpassword"
## client = new SmtpClient("smtp-mail.outlook.com", 587)


@app.route('/login', methods=['GET'])
def login_get():
    return render(login_form)


@app.route('/login', methods=['POST'])
def login_post():
    user = request.form['user']
    email = request.form['pwd']
    if user in users and users[user].password == pwd:
        set_cookie(user)  # ...
        generate_and_store_key()  # ...
        send_mail(user, key)  # ...
        return redirect('/auth')


@app.route('/auth', methods=['GET'])
def login_get():
    return render(auth_form)


@app.route('/auth', methods=['POST'])
def login_post():
    key = request.form['key']
    user = cookies_get_user()
    if user in users and users[user].key == key
        set_cookie(key)
        return redirect('/account')


@app.route('/setcookie', methods=['POST', 'GET'])
def set_cookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp