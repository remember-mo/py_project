# coding: utf-8

from flask import Flask

application = Flask("appOne")


@application.route("/home")
def home():
    return "appOne home"
