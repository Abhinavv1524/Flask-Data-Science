# Dynamic URL
# Variable Rules and URL Building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome user"

@app.route('/pass/<int:score>')
def passed(score):
    return "<html><body><h1>you have passed</h1></body></html>"

@app.route('/fail/<int:score>')
def failed(score):
    return "<html><body><h1>you have failed</h1></body></html>"

@app.route('/result/<int:score>')
def result(score):
    result = ""
    if score >=50:
        result = "passed"
    else:
        result = 'failed'
    
    return redirect(url_for(result,score=score))



if __name__ == '__main__':
    app.run(debug=True)
