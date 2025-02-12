from flask import Flask

### WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the page. This is the home page"

@app.route('/about')
def about():
    return "Welcome to the page. This is the about page"


if __name__ == '__main__':
    app.run(debug=True)