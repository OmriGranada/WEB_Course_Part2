from flask import Blueprint, render_template

# productsPage blueprint definition
productsPage = Blueprint('productsPage', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@productsPage.route('/productsPage')
def index():
    return render_template('productsPage.html')
