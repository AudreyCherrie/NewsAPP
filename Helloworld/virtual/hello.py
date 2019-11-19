from flask import Flask
app = Flask(__name__) # determines the route path of the app
@app.route('/')  # a decorator
def index():
    return '<h1>Hello World </h1>'

if _name_ == '_main_':
    app.run(debug = True)