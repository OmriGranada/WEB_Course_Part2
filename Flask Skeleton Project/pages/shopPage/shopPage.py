from flask import Blueprint, render_template

# shopPage blueprint definition
shopPage = Blueprint('shopPage', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@shopPage.route('/shopPage')
def index():
    return render_template('shopPage.html')
