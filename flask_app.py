from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app
import json

class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def say_hello(self):
        return "Hello " + self.name + "!!"

app = Flask(__name__)
app.config.from_object(__name__)

#TODO

# @app.route('/', methods=['GET', 'POST'])
# def index(name=""):
#     if request.method == 'POST':
#         name = request.form["name"]
#         # email = request.form["email"]
#         # data = Person(name, email).say_hello()
#         # return json.dumps({"data":data})
#     return render_template('index.html', name=name)
#
#
# @app.route('/profile/<username>')
# def profile(username):
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        data = Person(name, email).say_hello()
        return json.dumps({"data":data})

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)