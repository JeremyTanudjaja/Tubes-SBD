from flask import Flask

app = Flask(__name__)
app.config['EMPLOYEE_IMAGE_UPLOADS'] = "logic/static/res/employee_pic"
app.config['CUSTOMER_IMAGE_UPLOADS'] = "logic/static/res/customer_pic"
app.config['MATERIAL_IMAGE_UPLOADS'] = "logic/static/res/material_pic"
app.config['PRODUCT_IMAGE_UPLOADS'] = "logic/static/res/prod_pic"
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG', 'GIF']

from logic import routes