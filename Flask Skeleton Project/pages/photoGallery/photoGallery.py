from flask import Blueprint, render_template

# photoGallery blueprint definition
photoGallery = Blueprint('photoGallery', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@photoGallery.route('/photoGallery')
def index():
    return render_template('photoGallery.html')
