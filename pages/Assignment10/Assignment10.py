from flask import Flask, redirect, url_for
from flask import Blueprint, render_template
from flask import request, session
from interact_with_DB import interact_db

# Assignment10 blueprint definition
Assignment10 = Blueprint('Assignment10', __name__,
                        static_folder='static',
                        static_url_path='/Assignment10',
                        template_folder='templates')


# Routes
@Assignment10.route('/Assignment10')
def Assignment10_func():
    query = 'select * from users_10;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('Assignment10.html', users=users)

@Assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    user_id = request.form['id']
    new_name = request.form['newName']
    query = "UPDATE users_10 SET user_name = '%s' WHERE user_email='%s';" % (new_name, user_id)
    interact_db(query=query, query_type='commit')
    return redirect('/Assignment10')

@Assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users_10 WHERE user_email='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/Assignment10')

@Assignment10.route('/insert_user', methods = ['POST'])
def insert_user_func():
    # get the data
    email = request.form['email']
    name = request.form['name']
    # insert to db
    query = "INSERT INTO users_10(user_email, user_name) VALUES ('%s', '%s');" % (email, name)
    interact_db(query=query, query_type='commit')
    # come back to users page
    return redirect('/Assignment10')
