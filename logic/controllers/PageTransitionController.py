


class Transition_Controller:

    def __init__(self):
        print("Transition Controller Called")

    def login_admin(self, admin_data):
        admin_name = admin_data['name']
        admin_password = admin_data['password']
        if admin_name.lower() == "admin" and admin_password == "12345678":
            return True
        print("Login Failed")
        return False

