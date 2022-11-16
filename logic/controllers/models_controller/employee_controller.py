
class Employee_Controller():

    def __init__(self, cursor):
        '''Initialize the Department controller'''
        print("connection to Employee succeeded")
        self.cursor = cursor

    def get_employee_data(self):
        '''This Method will grab all the data from the department table'''
        data = []
        self.cursor.execute(
            f"select emp_id, full_name, email, phone_number, hire_date, salary, photo_link, manager_id, departmen_id "
            f"from vEmployees")
        for emp_id, full_name, email, phone_number, hire_date, salary, photo_link, manager_id, departmen_id in self.cursor:
            data.append({"employee_id": emp_id,
                         "employee_name": full_name,
                         "email": email,
                         "phone_number": phone_number,
                         "hire_date": hire_date,
                         "salary": salary,
                         "photo_link": photo_link,
                         "manager_id": manager_id,
                         "dept_id": departmen_id})
        # print(data)
        print(len(data))
        return data