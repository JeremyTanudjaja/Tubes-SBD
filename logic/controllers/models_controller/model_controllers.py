import cx_Oracle as oracle
from logic.controllers.models_controller import admin_controller
from logic.controllers.models_controller import department_controller
from logic.controllers.models_controller import employee_controller
from logic.controllers.models_controller import vendor_controller
from logic.controllers.models_controller import product_controller
from logic.controllers.models_controller import customer_controller
from logic.controllers.models_controller import material_controller
from logic.controllers.models_controller import inventory_controller
from logic.controllers.models_controller import material_order_controller
from logic.controllers.models_controller import sales_product_controller
from logic.controllers.models_controller import report_view

class Model_Controller:

    admins = None
    departments = None
    employees = None
    vendors = None
    products = None
    customers = None
    materials = None
    inventories = None
    material_orders = None
    sales_product = None
    report_view = None

    def __init__(self):
        """Initialize connection to oracle database and creates a cursor"""
        self.oracle = oracle
        self.oracle.init_oracle_client(lib_dir='D:\Development_res\ORACLE_INSTANT_LIBRARY\instantclient_19_16')
        self.conn = self.oracle.connect(user='TubesSBD', password='root', dsn='localhost')
        self.cursor = self.conn.cursor()
        print(self.conn.version)
        print(self.oracle.version)
        self.call_models()

    def call_models(self):
        """This Method is used to Initialized all the models so that we can manipulate the data
        in the HTML, basically this is the gateway for the SQL logic to pass through"""
        self.admins = admin_controller.Admin_Controller(cursor=self.cursor, oracle=self.oracle)
        self.departments = department_controller.Department_Controller(cursor=self.cursor, oracle=self.oracle)
        self.employees = employee_controller.Employee_Controller(cursor=self.cursor, oracle=self.oracle)
        self.vendors = vendor_controller.Vendor_Controller(cursor=self.cursor, oracle=self.oracle)
        self.products = product_controller.Product_Controller(cursor=self.cursor, oracle=self.oracle)
        self.customers = customer_controller.Customer_Controller(cursor=self.cursor, oracle=self.oracle)
        self.materials = material_controller.Material_Controller(cursor=self.cursor, oracle=self.oracle)
        self.inventories = inventory_controller.Inventory_Controller(cursor=self.cursor, oracle=self.oracle)
        self.sales_product = sales_product_controller.Sales_Product_Controller(cursor=self.cursor, oracle=self.oracle)
        self.material_orders = material_order_controller.Material_Order_Controller(cursor=self.cursor, oracle=self.oracle)
        self.report_view = report_view.Report_Controller(cursor=self.cursor, oracle=self.oracle)

