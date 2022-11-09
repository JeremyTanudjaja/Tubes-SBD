import cx_Oracle as oracle
from logic.controllers.models_controller import department_controller


class Model_Controller:

    departments = None
    employees = None
    vendors = None
    products = None
    customers = None
    materials = None
    inventories = None
    material_orders = None
    sales_product = None

    def __init__(self):
        '''Initialize connection to oracle database and creates a cursor'''
        oracle.init_oracle_client(lib_dir='D:\Development_res\ORACLE_INSTANT_LIBRARY\instantclient_19_16')
        self.conn = oracle.connect(user='TubesSBD', password='root', dsn='localhost')
        self.cursor = self.conn.cursor()
        print(self.conn.version)
        print(oracle.version)
        self.call_models()

    def call_models(self):
        '''This Method is used to Initialized all the models so that we can manipulate the data
        in the HTML, basicly this is the gateway for the SQL logic to pass through'''
        self.departments = department_controller.Department_Controller(cursor=self.cursor)

