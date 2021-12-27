from flask import Blueprint, render_template

# aboutUs blueprint definition
users = Blueprint('users', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@users.route('/users')
def users():
    return render_template('users.html')
