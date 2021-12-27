from flask import Blueprint, render_template

# contactUs blueprint definition
contactUs = Blueprint('contactUs', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@contactUs.route('/contactUs')
def index():
    return render_template('contactUs.html')
