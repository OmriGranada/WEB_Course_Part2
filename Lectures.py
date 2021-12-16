from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_page():
    # DB
    found = False
    if found:
        return render_template('index.html', name='Omri') # connects between the server to the html
    else:
        return render_template('index.html') # connects between the server to the html


@app.route('/about')
def about_func():
    # TODO
    name = 'Omri'
    secondName = 'Granada'
    uni = 'BGU'
    # return redirect('/catalog') # call for another route - catalog
    return render_template('about.html',
                           profile={'name':name, 'secondName':secondName}, # dictionary
                           university=uni, # string
                           degrees=['BSC', 'MSc'],# list
                           hobbies=('art', 'music', 'flask')) # tuple



@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html')

@app.route('/login')
def login_func():
    return redirect(url_for('home_func')) # call for another func - home

if __name__ == '__main__':
    app.run(debug=True)


"""
COMMENTS:
* i left
* GET (Select): it doesnt matter if we share the parameters we send
* POST (Insert): we dont want to share the parameters er send
* PUT (Update):
* DELETE:
* we use form in order to use those requests

"""