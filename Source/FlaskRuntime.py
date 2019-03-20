# coding: utf-8

from flask import Flask
import time


app = Flask(__name__)
idx = 0

@app.route("/a")
def a():
    global idx
    print("a："+str(idx)+"===="+str(time.time()))
    time.sleep(10)
    print("a："+str(idx)+"===="+str(time.time()))
    idx += 1
    return "a"


@app.route("/b")
def b():
    global idx
    print("b："+str(idx)+"===="+str(time.time()))
    time.sleep(7)
    print("b："+str(idx)+"===="+str(time.time()))
    idx += 1
    return "b"


@app.route("/index")
def index():
    return "index"


@app.route("/")
def home():
    return "home"


if __name__ == "__main__":
    app.run()
