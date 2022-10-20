import cx_Oracle as oracle
from flask_uploads import configure_uploads, IMAGES, UploadSet

class Controller_Test:

    def __init__(self):
        '''Initialize connection to oracle database and creates a cursor'''
        oracle.init_oracle_client(lib_dir='D:\Development_res\ORACLE_INSTANT_LIBRARY\instantclient_19_16')
        self.conn = oracle.connect(user='hr',password='root',dsn='localhost')
        self.cursor = self.conn.cursor()
        print(self.conn.version)
        print(oracle.version)

    def insert_data(self):
        pass

    def grab_data(self):
        '''Grabs a Data'''
        # Note: never use select * because it will throw an error 'too much data to unpack'
        data = []
        self.cursor.execute(f"select employee_id, first_name, last_name from employees where employee_id > {0} order by employee_id asc")
        for employee_id, first_name, last_name in self.cursor:
            # print(f"{employee_id} | {first_name} {last_name}")
            data.append({"id": employee_id, "name": first_name + ' ' +last_name})
        # print(data)
        # print(len(data))
        return data

