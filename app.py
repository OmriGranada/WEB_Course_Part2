from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/homePage')
@app.route('/')
def home_func():
    return render_template('index8.html')


@app.route('/Assignment8')
def Assignment8_func():
    #DB
    found = True
    name = 'Omri'
    secondName = 'Granada'
    uni = 'Ben Gurion University'
    if found:
        return render_template('Assignment8.html',
                           profile={'name':name, 'secondName':secondName}, # dictionary
                           university=uni, # string
                           hobbies=('Running', 'Flask', 'Scuba-Diving'), # tuple
                           logged='T')
    else:
        return render_template('Assignment8.html',
                           profile={'name':name, 'secondName':secondName}, # dictionary
                           university=uni, # string
                           hobbies=('Running', 'Flask', 'Scuba-Diving')) # tuple



if __name__ == '__main__':
    app.run(debug=True)

