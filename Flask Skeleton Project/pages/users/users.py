from flask import Blueprint, render_template

# about blueprint definition
about = Blueprint('users', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@about.route('/users')
def users():
    return render_template('users.html')
