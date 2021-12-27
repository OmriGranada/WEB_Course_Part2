from flask import Blueprint, render_template

# login blueprint definition
login = Blueprint('login', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')
