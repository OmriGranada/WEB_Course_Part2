from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home_func():
    return 'welcome to the main page'

@app.route('/about')
def about_func():
    # TODO
    return redirect('/catalog') # call for another route - catalog

@app.route('/catalog')
def catalog_func():
    return 'welcome to catalog'

@app.route('/login')
def login_func():
    return redirect(url_for('home_func')) # call for another func - home

if __name__ == '__main__':
    app.run()

