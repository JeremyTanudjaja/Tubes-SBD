import os
from werkzeug.utils import secure_filename
import shortuuid


class Employee_Controller():

    def __init__(self, cursor, oracle):
        '''Initialize the Department controller'''
        print("connection to Employee succeeded")
        self.cursor = cursor
        self.oracle = oracle

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

    # INSERTING FUNCTIONS
    def check_file_extension(self, filename, app):
        """To Check if the file is in correct format or not"""
        if "." not in filename:
            print("image must have an extension")
            return False
        ext = filename.rsplit(".", 1)[1]
        if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
            return True
        else:
            return False

    def sanitize_file_name(self, filename):
        """ Make a Unique Filename and get rid of any bad names
        like ../../../movie.mov becomes movie.mov, etc"""
        ext = filename.rsplit(".", 1)[1]
        image_name = filename.split(".")[0]
        new_filename = f"{image_name}{shortuuid.uuid()}.{ext}"
        sanitized_file_name = secure_filename(new_filename)
        return sanitized_file_name

    def insert_new_employee(self, data, image, app):
        """Inserting a new employee"""

        # INSERTING THE FILENAME TO A FOLDER
        if image.filename == "":
            print("Image must have a filename")
            return "Error Image must have a filename"
        else:
            if not self.check_file_extension(image.filename, app):
                print("The Extension is not allowed")
                return "Image have bad extension type"
        filename = self.sanitize_file_name(image.filename)

        image.save(os.path.join(app.config['EMPLOYEE_IMAGE_UPLOADS'], filename))
        # SAVING EMPLOYEE DATA
        try:
            print("masuk insertion")
            # print(data['Hire_Date'])
            # print(f"CALL NEWEMP('{data['Employee_Name']}','{data['Email']}',"
            #                     f"'{data['Phone_Number']}','{data['Hire_Date']}',{data['Salary']},"
            #                     f"'{data['Manager_ID']}','{data['Department_ID']}','{filename}')")
            self.cursor.execute(f"CALL newEmp('{data['Employee_Name']}','{data['Email']}',"
                                f"'{data['Phone_Number']}','{data['Hire_Date']}',{data['Salary']},"
                                f"'{data['Manager_ID']}','{data['Department_ID']}','{filename}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    # ---------------------------------------------------------------

    def grab_photo_link(self, id):
        """Grab Photo Link from employee database"""
        emp_id = id
        link = None
        self.cursor.execute(f"select photo_link from employees where EMP_ID = {emp_id}")
        for photo_link in self.cursor:
            link = photo_link
        return link

    def delete_photo(self, photo_link, app):
        """Delete Photo from folder"""
        print(photo_link)
        try:
            os.remove(f"{app.config['EMPLOYEE_IMAGE_UPLOADS']}/{photo_link}")
        except FileNotFoundError as e:
            error_message = f"{e}"
            return error_message
        return "success delete"

    def grab_date(self, id):
        emp_id = id
        date = None
        self.cursor.execute(f"select hire_date from employees where EMP_ID = {emp_id}")
        for hire_date in self.cursor:
            date = hire_date
        return date

    # UPDATE EMPLOYEES

    def update_employee_data(self, id, image, data, app):
        """Update Employee Data"""
        emp_id = id

        # Grab Old employee photo link
        photo_link = self.grab_photo_link(emp_id)[0]

        # INSERTING THE FILENAME/PHOTO TO A FOLDER
        if image.filename == "":
            # Get Old Photo Link if there's no photo
            filename = photo_link
            print("No Image")
        else:
            # Insert Photo to Folder
            if not self.check_file_extension(image.filename, app):
                print("The Extension is not allowed")
                return "Image have bad extension type"
            filename = self.sanitize_file_name(image.filename)
            image.save(os.path.join(app.config['EMPLOYEE_IMAGE_UPLOADS'], filename))

            # Delete Old Photo if there's a new photo
            print(self.delete_photo(photo_link, app))

        # Check if Date is empty or not
        date = data['Hire_Date'].split(' ')[0]

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"CALL UpdEmp("
                                f"{emp_id}, '{data['Employee_Name']}', '{data['Email']}',"
                                f"'{data['Phone_Number']}', '{date}', {data['Salary']},"
                                f"'{filename}', '{data['Manager_ID']}',"
                                f"'{data['Department_ID']}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"



    # DELETION FUNCTIONS
    def delete_employee(self, id, app):
        """Delete a Employee From Reality"""
        # DELETE EMPLOYEE IMAGE
        emp_id = id
        photo_link = self.grab_photo_link(emp_id)[0]

        print(self.delete_photo(photo_link, app))


        try:
            self.cursor.execute(f"Delete from employees where EMP_ID = {emp_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"

    # -----------------------------------------
