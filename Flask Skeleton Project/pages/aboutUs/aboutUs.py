from flask import Blueprint, render_template

# aboutUsUs blueprint definition
aboutUs = Blueprint('aboutUs', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@aboutUs.route('/aboutUs')
def index():
    return render_template('aboutUs.html')
