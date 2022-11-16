class Admin_Controller():

    def __init__(self, cursor):
        """Initialize the Admin controller"""
        print("connection to Admin succeeded")
        self.cursor = cursor

    def get_admin_data(self):
        """This Method will grab all the data from the Admin table"""
        data = []
        self.cursor.execute(
            f"select admin_id, username, password, emp_id from Admins")
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
        login_data = []
        self.cursor.execute(f"select admin_id, password from Admins where username = '{username}'")
        for admin_id, password in self.cursor:
            login_data.append({"admin_id": admin_id,
                               "password": password})
        if len(login_data) == 0:
            return False
        else:
            return login_data
