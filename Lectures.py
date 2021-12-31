from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
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
    if 'user_inside' in session:
        if session['user_inside']:
            print('user inside')
    if 'product' in request.args: # check if the form is filled
        product = request.args['product'] # gets the value of the "name" from html
        size = request.args['size']
        return render_template('catalog.html', p_name = product, p_size = size)
    return render_template('catalog.html')

@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('index.html')

@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # insert to db
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s');" % (name, email, password)
    interact_db(query = query, query_type='commit')
    # come back to users page
    return redirect('/users')

@app.route('/users')
def users_func():
    query = 'select * from users;'
    users = interact_db(query = query, query_type='fetch' )
    return render_template('users.html', users = users)

@app.route('/login', methods=['GET', 'POST']) # need both get (for the first time) & post
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username'] # POST -> form, GET -> args
        password = request.form['password']
        # DB
        found = True
        if found:
            session['username'] = username
            session['user_inside'] = True
            return redirect(url_for('home_func'))
        else:
            render_template('login.html')


app.route('/req_frontend')
def req_frontend_func():
    return render_template('req_frontend.html')

app.route('/req_backend')
def req_backend_func():
    return render_template('req_backend.html')

if __name__ == '__main__':
    app.run(debug=True)


"""
COMMENTS:
* i left
* GET (Select): it doesnt matter if we share the parameters we send
* POST (Insert): we dont want to share the parameters we send
* PUT (Update):
* DELETE:
* we use form in order to use those requests

* blue prints

"""