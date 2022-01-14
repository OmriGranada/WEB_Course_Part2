from flask import Flask, redirect, url_for, render_template
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import *
import requests
import random
from flask import jsonify
import asyncio
# import aiohttp

app = Flask(__name__)
app.secret_key ='123' # must be when we use session, for every project

from pages.Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)

# Create list of users as a dictionary
users = {'user1': {'name': 'Drori', 'email': 'drori@gmail.com'},
         'user2': {'name': 'Orit', 'email': 'orit@gmail.com'},
         'user3': {'name': 'Yotam', 'email': 'yotam@gmail.com'},
         'user4': {'name': 'Omri', 'email': 'omri@gmail.com'},
         'user5': {'name': 'Amitay', 'email': 'amitay@gmail.com'}}

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

@app.route('/LogOut')
def LogOut_func():
    session['username'] = ''
    return render_template('Assignment9.html')

def find_user(given_email):
    print(given_email)
    for user_number, user_details in users.items():
        if user_details['email'] == given_email:
            print('user found!!!!!!!!!!!!!!')
            return user_details['name'], user_details['email']
    print('didnt find user')
    return False


@app.route('/Assignment9', methods=['GET', 'POST'])
def Assignment9_func():
    if request.method == 'GET':
        # SEARCH form
        if 'user_email' in request.args:
            if (find_user(request.args['user_email']) != False):
                result_name = find_user(request.args['user_email'])[0]
                result_email = find_user(request.args['user_email'])[1]
                return render_template('Assignment9.html', result_name=result_name, result_email=result_email)
            return render_template('Assignment9.html', users_List=users)# in case the email is incorrect or empty all of the esers will be displayed
    if request.method == 'POST':
        # REGISTER form
        username = request.form['username']
        # password = request.form['password']
        # DB
        found = True
        if found: # fictive check
            session['username'] = username
            # session['user_inside'] = True
            return render_template('Assignment9.html')
    return render_template('Assignment9.html')

@app.route('/Assignment11')
def Assignment11_func():
    return render_template('Assignment11.html')

@app.route('/Assignment11/users')
def assignment11_users_fun():
    return_dict = {}
    query = 'select * from users_10;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict[f'user_{user.user_email}'] = {
            'status': 'success',
            'name': user.user_name,
            'email': user.user_email,
        }
    return jsonify(return_dict)

# @app.route('/Assignment11/outer_source')
# def assignment11_outer_source_fun():
#     return render_template('/outer_source.html')


def get_user(id):
    users = []
    if (id != ""): # in case there is id
        user_id = int(id)
        res = requests.get(f'https://reqres.in/api/users/{user_id}')
        res = res.json()
        users.append(res)
    else: # there is no ID - return all users
        length = len(requests.get(f'https://reqres.in/api/users').json()['data'])
        for i in range(1, length+1):
            res = requests.get(f'https://reqres.in/api/users/{i}')
            res = res.json()
            users.append(res)
    return users

@app.route('/Assignment11/outer_source')
def Assignment11_outer_source_func():
    users = get_user("")
    if "user_id" in request.args:
        user_id = request.args['user_id']
        users = get_user(user_id)
    return render_template('Assignment11.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)

