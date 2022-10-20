from flask import render_template, url_for, flash, redirect, session, app
from logic.controller import Controller_Test
from logic import app

test = Controller_Test()

@app.route("/home")
@app.route("/")
def home():
    test_data = test.grab_data()
    return render_template("index.html", employees=test_data)
