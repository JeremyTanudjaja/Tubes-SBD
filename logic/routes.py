from flask import render_template, redirect, request
from logic.controllers.PageTransitionController import Transition_Controller
from logic.controllers.models_controller.model_controllers import Model_Controller
from logic import app

page_controller = Transition_Controller()
model_controller = Model_Controller()
admin_data_for_page = None


@app.route("/", methods=['POST', 'GET'])
def index():
    global admin_data_for_page
    if request.method == "POST":
        request_data = request.form
        name = request_data['name']
        # print(f"Name:{request_data['name']}\nPass:{request_data['password']}")
        admin_data = model_controller.admins.get_login_data(username=name)
        if admin_data == False:
            return redirect("/")
        # print(admin_data)
        if page_controller.login_admin(login_data=request_data, admin_data=admin_data):
            admin_data_for_page = {'ID': admin_data[0]['admin_id'],
                                   'name': request_data['name']}
            # print(admin_data_for_page)
            return redirect("/home")
    admin_data_for_page = None
    return render_template("index.html")


@app.route("/home", methods=['POST', 'GET'])
def home():
    # print(admin_data_for_page)
    return render_template("home.html", admin_data=admin_data_for_page)


# ADMIN
@app.route("/Admin", methods=['POST', 'GET'])
def admins():
    # if request.method == 'POST':
    #     print(request.form)
    #     request_data = request.form
    #     result = model_controller.admins.insert_new_admin(request_data)
    #     print(result)
    admin_datas = model_controller.admins.get_admin_data()
    # print(admin_datas)
    return render_template("page_init/admin_init.html", data=admin_datas)


@app.route("/Insert_Admin", methods=['POST', 'GET'])
def insert_admin():
    if request.method == 'POST':
        print(request.form)
        request_data = request.form
        result = model_controller.admins.insert_new_admin(request_data)
        print(result)
        return redirect('/home')


@app.route("/Load_Update_Admin", methods=['POST', 'GET'])
def load_update_admin():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/admin_update.html", data=request_data)
    return render_template("update/admin_update.html")


@app.route("/Update_Admin", methods=['POST', 'GET'])
def update_admin():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Admin_ID']
        print(request_data)
        result = model_controller.admins.update_admin(id, request_data)
        print(result)
        return redirect('/home')


@app.route("/delete_admin/<id>", methods=['POST', 'GET'])
def delete_admin(id):
    # print(f"masuk delete Admin :{id}")
    result = model_controller.admins.delete_admin(id)
    print(result)
    return redirect('/home')


# ----------------------------------------------


# DEPARTMENT
@app.route("/Departments", methods=['POST', 'GET'])
def departments():
    # print(dept_data)
    dept_data = model_controller.departments.get_department_data()
    return render_template("page_init/departments_init.html", dept_data=dept_data)


@app.route("/insert_into_department", methods=['POST', 'GET'])
def insert_department():
    if request.method == 'POST':
        request_data = request.form
        result = model_controller.departments.insert_new_department(request_data)
        print(result)
        return redirect("/home")


@app.route("/Load_Update_Department", methods=['POST', 'GET'])
def load_update_department():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/departments_update.html", data=request_data)
    return render_template("update/departments_update.html")


@app.route("/Update_Department", methods=['POST', 'GET'])
def update_department():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Department_ID']
        result = model_controller.departments.update_department(id, request_data)
        print(result)
        return redirect('/home')


@app.route("/Delete_Department/<id>", methods=['POST', 'GET'])
def delete_department(id):
    result = model_controller.departments.delete_department(id)
    print(result)
    return redirect('/home')


# ------------------------------------------------------

# EMPLOYEES
@app.route("/Employees", methods=['POST', 'GET'])
def employees():
    employee_data = model_controller.employees.get_employee_data()
    # print(employee_data)
    return render_template("page_init/employee_init.html", data=employee_data)


@app.route("/insert_employees", methods=['POST', 'GET'])
def insert_employees():
    print("masuk routes insert_employees")
    if request.method == "POST":
        print("masuk request.method = post ")
        if request.files:
            print("masuk request files employees photo")
            image = request.files['Employee_Photo']
            request_data = request.form
            result = model_controller.employees.insert_new_employee(data=request_data, image=image, app=app)
            print(result)
    return redirect("/home")


@app.route("/load_update_employee", methods=['POST', 'GET'])
def load_update_employee():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/employee_update.html", data=request_data)
    return render_template("update/employee_update.html")


@app.route("/update_employee", methods=["POST", "GET"])
def update_employee():
    if request.method == "POST":
        request_data = request.form
        id = request_data['emp_id']
        image = request.files['Employee_Photo']
        result = model_controller.employees.update_employee_data(id=id, image=image, data=request_data, app=app)
        print(result)
        return redirect("/home")


@app.route("/delete_employee/<id>", methods=["POST", "GET"])
def delete_employee(id):
    result = model_controller.employees.delete_employee(id, app)
    print(result)
    return redirect("/home")


# ----------------------------------------------------------

# PRODUCTS
@app.route("/Product", methods=['POST', 'GET'])
def products():
    product_data = model_controller.products.get_product_data()
    return render_template("page_init/products_init.html", data=product_data)


@app.route("/Insert_Product", methods=['POST', 'GET'])
def insert_product():
    print("masuk routes insert_product")
    if request.method == "POST":
        print("masuk request.method = post ")
        if request.files:
            print("masuk request files product photo")
            image = request.files['Product_Photo']
            request_data = request.form
            result = model_controller.products.insert_new_product(data=request_data, image=image, app=app)
            print(result)
    return redirect("/home")


@app.route("/Load_Update_Product", methods=['POST', 'GET'])
def load_update_product():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/product_update.html", data=request_data)
    return render_template("update/product_update.html")


@app.route("/Update_Product", methods=['POST', 'GET'])
def update_product():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Product_ID']
        print(id)
        image = request.files['Product_Photo']
        result = model_controller.products.update_product_data(id=id, image=image, data=request_data, app=app)
        print(result)
        return redirect("/home")


@app.route("/Delete_Product/<id>", methods=['POST', 'GET'])
def delete_product(id):
    result = model_controller.products.delete_product(id, app)
    print(result)
    return redirect('/home')


# ------------------------------------------------------------------

# INVENTORIES
@app.route("/Inventories", methods=['POST', 'GET'])
def inventories():
    inventory_data = model_controller.inventories.get_inventory_data()
    # print(inventory_data)
    return render_template("page_init/inventories_init.html", data=inventory_data)


@app.route("/Insert_Inventories", methods=['POST', 'GET'])
def insert_inventories():
    if request.method == "POST":
        request_data = request.form
        result = model_controller.inventories.insert_inventory(request_data)
        print(result)
    return redirect('/home')


@app.route("/Load_Update_Inventories", methods=['POST', 'GET'])
def load_update_inventories():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/inventories_update.html", data=request_data)
    return render_template("update/inventories_update.html")


@app.route("/Update_Inventories", methods=['POST', 'GET'])
def update_inventories():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Product_ID']
        result = model_controller.inventories.update_inventory(id, request_data)
        print(result)
        return redirect('/home')


@app.route("/Delete_Inventories/<id>", methods=['POST', 'GET'])
def delete_inventories(id):
    result = model_controller.inventories.delete_inventory(id)
    print(result)
    return redirect('/home')


# -------------------------------------------------------------

# VENDORS
@app.route("/Vendor", methods=['POST', 'GET'])
def vendors():
    vendor_data = model_controller.vendors.get_vendor_data()
    # print(vendor_data)
    return render_template("page_init/vendor_init.html", data=vendor_data)


@app.route("/insert_vendor", methods=["POST", "GET"])
def insert_vendor():
    if request.method == "POST":
        request_data = request.form
        result = model_controller.vendors.insert_new_vendor(request_data)
        print(result)
    return redirect("/home")


@app.route("/load_update_vendor", methods=["POST", "GET"])
def load_update_vendor():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/vendor_update.html", data=request_data)
    return render_template("update/vendor_update.html")


@app.route("/update_vendor", methods=["POST", "GET"])
def update_vendor():
    if request.method == "POST":
        request_data = request.form
        id = request_data['update_vendor_id']
        result = model_controller.vendors.update_vendor(id=id, data=request_data)
        print(result)
        return redirect("/home")


@app.route("/delete_vendor/<id>", methods=["POST", "GET"])
def delete_vendor(id):
    result = model_controller.vendors.delete_vendor(id)
    print(result)
    return redirect("/home")


# --------------------------------------------------------------------

# MATERIALS
@app.route("/Material", methods=['POST', 'GET'])
def materials():
    material_data = model_controller.materials.get_material_data()
    # print(material_data)
    return render_template("page_init/materials_init.html", data=material_data)


@app.route("/Insert_Material", methods=['POST', 'GET'])
def insert_material():
    if request.method == "POST":
        print("masuk request.method = post ")
        if request.files:
            print("masuk request files Material photo")
            image = request.files['Material_Photo']
            request_data = request.form
            result = model_controller.materials.insert_new_material(data=request_data, image=image, app=app)
            print(result)
            return redirect('/home')


@app.route("/Load_Update_Material", methods=['POST', 'GET'])
def load_update_material():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/material_update.html", data=request_data)
    return render_template("update/material_update.html")


@app.route("/Update_Material", methods=['POST', 'GET'])
def update_material():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Material_ID']
        image = request.files['Material_Photo']
        result = model_controller.materials.update_material_data(id=id, image=image, data=request_data, app=app)
        print(result)
        return redirect("/home")


@app.route("/Delete_Material/<id>", methods=['POST', 'GET'])
def delete_material(id):
    result = model_controller.materials.delete_material(id, app)
    print(result)
    return redirect('/home')


# -------------------------------------------------------------------

# MATERIAL ORDERS
@app.route("/Material_Order", methods=['POST', 'GET'])
def material_orders():
    materials_order_data = model_controller.material_orders.get_material_order_data()
    # print(materials_order_data)
    return render_template("page_init/material_order_init.html", data=materials_order_data)


@app.route("/Insert_Material_Order", methods=['POST', 'GET'])
def insert_material_order():
    if request.method == "POST":
        request_data = request.form
        result = model_controller.material_orders.insert_new_material_order(request_data)
        print(result)
    return redirect("/home")


@app.route("/Load_Update_Material_Order", methods=['POST', 'GET'])
def load_update_material_order():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/material_order_update.html", data=request_data)
    return render_template("update/material_order_update.html")


@app.route("/Update_Material_Order", methods=['POST', 'GET'])
def update_material_order():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Order_ID']
        result = model_controller.material_orders.update_material_order(id=id, data=request_data)
        print(result)
        return redirect("/home")


@app.route("/Delete_Material_Order/<id>", methods=['POST', 'GET'])
def delete_material_order(id):
    result = model_controller.material_orders.delete_material_order(id)
    print(result)
    return redirect("/home")


# ------------------------------------------------------------------

# CUSTOMER
@app.route("/Customer", methods=['POST', 'GET'])
def customers():
    customer_data = model_controller.customers.get_customer_data()
    return render_template("page_init/customer_init.html", data=customer_data)


@app.route("/Insert_Customer", methods=['POST', 'GET'])
def insert_customer():
    print("masuk routes insert_customer")
    if request.method == "POST":
        print("masuk request.method = post ")
        if request.files:
            print("masuk request files customer photo")
            image = request.files['Profile_Photo']
            request_data = request.form
            result = model_controller.customers.insert_new_customer(data=request_data, image=image, app=app)
            print(result)
    return redirect("/home")


@app.route("/Load_Update_Customer", methods=['POST', 'GET'])
def load_update_customer():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/customer_update.html", data=request_data)
    return render_template("update/customer_update.html")


@app.route("/Update_Customer", methods=['POST', 'GET'])
def update_customer():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Customer_ID']
        image = request.files['Profile_Path']
        result = model_controller.customers.update_customer_data(id=id, image=image, data=request_data, app=app)
        print(result)
        return redirect("/home")


@app.route("/Delete_Customer/<id>", methods=['POST', 'GET'])
def delete_customer(id):
    result = model_controller.customers.delete_customer(id, app)
    print(result)
    return redirect('/home')


# ------------------------------------------------------------------

# SALES
@app.route("/Sales", methods=['POST', 'GET'])
def sales_product():
    sales_data = model_controller.sales_product.get_sales_product_data()
    # print(sales_data)
    return render_template("page_init/sales_product_init.html", data=sales_data)


@app.route("/Insert_Sales_Product", methods=['POST', 'GET'])
def insert_sales_product():
    if request.method == "POST":
        request_data = request.form
        result = model_controller.sales_product.insert_new_sales_product(request_data)
        print(result)
    return redirect("/home")


@app.route("/Load_Update_Sales_Product", methods=['POST', 'GET'])
def load_update_sales_product():
    if request.method == "POST":
        request_data = request.form
        print(request_data)
        return render_template("update/sales_product_update.html", data=request_data)
    return render_template("update/sales_product_update.html")


@app.route("/Update_Sales_Product", methods=['POST', 'GET'])
def update_sales_product():
    if request.method == "POST":
        request_data = request.form
        id = request_data['Sales_ID']
        result = model_controller.sales_product.update_sales_product(id=id, data=request_data)
        print(result)
        return redirect("/home")


@app.route("/Delete_Sales_Product/<id>", methods=['POST', 'GET'])
def delete_sales_product(id):
    result = model_controller.sales_product.delete_sales_product(id)
    print(result)
    return redirect('/home')
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Routes for Report
@app.route("/Report_Dashboard")
def load_report_page():
    return render_template('report/report_page.html')


