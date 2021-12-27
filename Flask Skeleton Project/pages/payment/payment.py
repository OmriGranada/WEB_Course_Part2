from flask import Blueprint, render_template

# payment blueprint definition
payment = Blueprint('payment', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@payment.route('/payment')
def index():
    return render_template('payment.html')
