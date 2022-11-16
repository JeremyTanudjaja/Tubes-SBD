


class Transition_Controller:

    def __init__(self):
        """Logic For Login to Page"""
        print("Transition Controller Called")

    def login_admin(self, login_data, admin_data):
        login_password = login_data['password']
        admin_password = admin_data[0]['password']
        if admin_password == login_password:
            return True
        print("Login Failed Password salah")
        return False

