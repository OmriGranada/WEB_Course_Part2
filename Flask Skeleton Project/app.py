from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## About
from pages.aboutUs.aboutUs import aboutUs # this line imports the object aboutUs from the path
app.register_blueprint(aboutUs) # connection between the application (app) to the blueprint (aboutUs)

## contactUs
from pages.contactUs.contactUs import contactUs
app.register_blueprint(contactUs)

## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## login
from pages.login.login import login
app.register_blueprint(login)

## payment
from pages.payment.payment import payment
app.register_blueprint(payment)

## photoGallery
from pages.photoGallery.photoGallery import photoGallery
app.register_blueprint(photoGallery)

## productsPage
from pages.productsPage.productsPage import productsPage
app.register_blueprint(productsPage)

## Q_and_A
from pages.Q_and_A.Q_and_A import Q_and_A
app.register_blueprint(Q_and_A)

## recipesPage
from pages.recipesPage.recipesPage import recipesPage
app.register_blueprint(recipesPage)

## shopPage
from pages.shopPage.shopPage import shopPage
app.register_blueprint(shopPage)

## tours
from pages.tours.tours import tours
app.register_blueprint(tours)

"""
## Users
from pages.users.users import users
app.register_blueprint(users)


## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)
"""



"""
###### Components
## footer
from components.footer.footer import footer
app.register_blueprint(footer)

## header
from components.header.header import header
app.register_blueprint(header)
"""







