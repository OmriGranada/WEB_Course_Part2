from flask import Blueprint, render_template

# Q_and_A blueprint definition
Q_and_A = Blueprint('Q_and_A', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@Q_and_A.route('/Q_and_A')
def index():
    return render_template('Q_and_A.html')
