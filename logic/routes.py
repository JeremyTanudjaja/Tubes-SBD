from flask import render_template, redirect, request
from logic.controllers.PageTransitionController import Transition_Controller
from logic.controllers.models_controller.model_controllers import Model_Controller
from logic import app

page_controller = Transition_Controller()
model_controller = Model_Controller()
admin_data = None


@app.route("/", methods=['POST', 'GET'])
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


@app.route("/home", methods=['POST', 'GET'])
def home():
    print(admin_data)
    return render_template("home.html", admin_data=admin_data)

@app.route("/Admin", methods=['POST', 'GET'])
def admins():
    admin_datas = model_controller.admins.get_admin_data()
    print(admin_datas)
    return render_template("page_init/admin_init.html", data=admin_datas)

@app.route("/Departments", methods=['POST', 'GET'])
def departments():
    dept_data = model_controller.departments.get_department_data()
    # print(dept_data)
    return render_template("page_init/departments_init.html", dept_data=dept_data)


@app.route("/Employees", methods=['POST', 'GET'])
def employees():
    employee_data = model_controller.employees.get_employee_data()
    # print(employee_data)
    return render_template("page_init/employee_init.html", data=employee_data)


@app.route("/Product", methods=['POST', 'GET'])
def products():
    product_data = model_controller.products.get_product_data()
    # print(product_data)
    return render_template("page_init/products_init.html", data=product_data)


@app.route("/Inventories", methods=['POST', 'GET'])
def inventories():
    inventory_data = model_controller.inventories.get_inventory_data()
    # print(inventory_data)
    return render_template("page_init/inventories_init.html", data=inventory_data)


@app.route("/Vendor", methods=['POST', 'GET'])
def vendors():
    vendor_data = model_controller.vendors.get_vendor_data()
    # print(vendor_data)
    return render_template("page_init/vendor_init.html", data=vendor_data)


@app.route("/Material", methods=['POST', 'GET'])
def materials():
    material_data = model_controller.materials.get_material_data()
    # print(material_data)
    return render_template("page_init/materials_init.html", data=material_data)


@app.route("/Material_Order", methods=['POST', 'GET'])
def material_orders():
    materials_order_data = model_controller.material_orders.get_material_order_data()
    # print(materials_order_data)
    return render_template("page_init/material_order_init.html", data=materials_order_data)


@app.route("/Customer", methods=['POST', 'GET'])
def customers():
    customer_data = model_controller.customers.get_customer_data()
    # print(customer_data)
    return render_template("page_init/customer_init.html", data=customer_data)


@app.route("/Sales", methods=['POST', 'GET'])
def sales_product():
    sales_data = model_controller.sales_product.get_sales_product_data()
    # print(sales_data)
    return render_template("page_init/sales_product_init.html", data=sales_data)
