
class Department_Controller():

    def __init__(self, cursor):
        '''Initialize the Department controller'''
        print("connection to Department succeeded")
        self.cursor = cursor

    def get_department_data(self):
        '''This Method will grab all the data from the department table'''
        data = []
        self.cursor.execute(
            f"select departmen_id, departmen_name, manager_id from vDepartments")
        for departmen_id, departmen_name, manager_id in self.cursor:
            # print(f"{employee_id} | {first_name} {last_name}")
            data.append({"dept_id": departmen_id,
                         "dept_name": departmen_name,
                         "manager_id": manager_id})
        # print(data)
        print(len(data))
        return data