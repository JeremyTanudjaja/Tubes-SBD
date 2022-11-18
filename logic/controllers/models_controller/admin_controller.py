class Admin_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Admin controller"""
        print("connection to Admin succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_admin_data(self):
        """This Method will grab all the data from the Admin table"""
        data = []
        self.cursor.execute(
            f"select admin_id, username, password, emp_id from vAdmin")
        print(self.cursor)
        for admin_id, username, password, emp_id in self.cursor:
            data.append({"admin_id": admin_id,
                         "username": username,
                         "password": password,
                         "emp_id": emp_id})
        # print(data)
        print(len(data))
        return data

    def get_login_data(self, username):
        """This Method is used to login in index page, it will get password, id from username
        data that was inputted from login form"""
        login_data = []
        self.cursor.execute(f"select admin_id, password from Admins where username = '{username}'")
        for admin_id, password in self.cursor:
            login_data.append({"admin_id": admin_id,
                               "password": password})
        if len(login_data) == 0:
            return False
        else:
            return login_data

    def insert_new_admin(self, data):
        """This method will call insert procedure to the admin table"""
        username = data['Admin_Username']
        password = data['Admin_Password']
        emp_id = data['Admin_EmployeeID']
        try:
            self.cursor.execute(f"CALL NewAdmin('{username}','{password}','{emp_id}')")
        except self.oracle.DatabaseError as e:
            error_message = f"{e.args}"
            return error_message
        else:
            return "Data Successfully Added"


