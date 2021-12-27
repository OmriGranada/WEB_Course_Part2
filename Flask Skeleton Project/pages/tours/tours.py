from flask import Blueprint, render_template

# tours blueprint definition
tours = Blueprint('tours', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@tours.route('/tours')
def index():
    return render_template('tours.html')
