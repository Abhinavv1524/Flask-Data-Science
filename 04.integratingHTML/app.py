# Integrating HTML with Flask
# HTTP - GET and Post

from flask import Flask, redirect, url_for,render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    return render_template('result.html',result = score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    totalScore = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['Maths'])
        cpp = float(request.form['C++'])
        machineLearning = float(request.form['Machine-Learning'])

        totalScore = (science + maths + cpp + machineLearning)/4

    return redirect(url_for('result',score =totalScore))


if __name__ == '__main__':
    app.run(debug=True)