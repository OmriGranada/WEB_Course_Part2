from flask import Blueprint, render_template

# recipesPage blueprint definition
recipesPage = Blueprint('recipesPage', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@recipesPage.route('/recipesPage')
def index():
    return render_template('recipesPage.html')
