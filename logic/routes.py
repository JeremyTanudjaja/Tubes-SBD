from flask import render_template, redirect, request
from logic.controllers.PageTransitionController import Transition_Controller
from logic.controllers.models_controller.model_controllers import Model_Controller
from logic import app


page_controller = Transition_Controller()
model_controller = Model_Controller()
admin_data = None

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == "POST":
        request_data = request.form
        print(f"Name:{request_data['name']}\nPass:{request_data['password']}")
        if page_controller.login_admin(request_data):
            global admin_data
            admin_data = {'ID': 1001,
                          'name': request_data['name']}
            print(admin_data)
            return redirect("/home")
    return render_template("index.html")

@app.route("/home", methods=['POST','GET'])
def home():
    print(admin_data)
    return render_template("home.html", admin_data = admin_data)

@app.route("/Departments", methods = ['POST','GET'])
def departments():
    dept_data = model_controller.department.get_department_data()
    print(dept_data)
    return render_template("page_init/departments_init.html", dept_data=dept_data)

@app.route("/Employees", methods = ['POST','GET'])
def employees():
    return render_template("page_init/employee_init.html")

@app.route("/Product", methods = ['POST','GET'])
def products():
    return render_template("page_init/products_init.html")

@app.route("/Inventories", methods = ['POST','GET'])
def inventories():
    return render_template("page_init/inventories_init.html")

@app.route("/Vendor", methods = ['POST','GET'])
def vendors():
    return render_template("page_init/vendor_init.html")

@app.route("/Material", methods = ['POST','GET'])
def materials():
    return render_template("page_init/materials_init.html")

@app.route("/Material_Order", methods = ['POST','GET'])
def material_orders():
    return render_template("page_init/material_order_init.html")

@app.route("/Customer", methods = ['POST','GET'])
def customers():
    return render_template("page_init/customer_init.html")

@app.route("/Sales", methods = ['POST','GET'])
def sales_product():
    return render_template("page_init/sales_product_init.html")