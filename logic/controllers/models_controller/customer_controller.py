import os
import shortuuid
from werkzeug.utils import secure_filename


class Customer_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Customer controller"""
        print("connection to Customer succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_customer_data(self):
        """This Method will grab all the data from the Customer table"""
        data = []
        self.cursor.execute(
            f"select customer_id, customer_name, address, profile_image_link from vCustomers")
        for customer_id, customer_name, address, profile_image_link in self.cursor:
            data.append({"customer_id": customer_id,
                         "customer_name": customer_name,
                         "address": address,
                         "image_link": profile_image_link})
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

    def insert_new_customer(self, data, image, app):
        """Inserting a new Customer"""

        # INSERTING THE FILENAME TO A FOLDER
        if image.filename == "":
            print("Image must have a filename")
            return "Error Image must have a filename"
        else:
            if not self.check_file_extension(image.filename, app):
                print("The Extension is not allowed")
                return "Image have bad extension type"
        filename = self.sanitize_file_name(image.filename)

        image.save(os.path.join(app.config['CUSTOMER_IMAGE_UPLOADS'], filename))
        # SAVING EMPLOYEE DATA
        try:
            print("masuk insertion")
            self.cursor.execute(f"CALL newCust('{data['Customer_Name']}','{data['Customer_Address']}',"
                                f"'{filename}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    # ---------------------------------------------------------------

    def grab_photo_link(self, id):
        """Grab Photo Link from customer database"""
        cust_id = id
        link = None
        self.cursor.execute(f"select PROFILE_IMAGE_LINK from customers where CUSTOMER_ID = {cust_id}")
        for photo_link in self.cursor:
            link = photo_link
        return link

    def delete_photo(self, photo_link, app):
        """Delete Photo from folder"""
        print(photo_link)
        try:
            os.remove(f"{app.config['CUSTOMER_IMAGE_UPLOADS']}/{photo_link}")
        except FileNotFoundError as e:
            error_message = f"{e}"
            return error_message
        return "success delete"

    # UPDATE EMPLOYEES

    def update_customer_data(self, id, image, data, app):
        """Update Employee Data"""
        cust_id = id

        # Grab Old employee photo link
        photo_link = self.grab_photo_link(cust_id)[0]

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
            image.save(os.path.join(app.config['CUSTOMER_IMAGE_UPLOADS'], filename))

            # Delete Old Photo if there's a new photo
            print(self.delete_photo(photo_link, app))

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"update customers set "
                                f"CUSTOMER_NAME='{data['Customer_Name']}',"
                                f"ADDRESS='{data['Customer_Address']}',"
                                f"PROFILE_IMAGE_LINK='{filename}'"         
                                f"where CUSTOMER_ID={cust_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"



    # DELETION FUNCTIONS
    def delete_customer(self, id, app):
        """Delete a Customer From Reality"""
        # DELETE EMPLOYEE IMAGE
        cust_id = id
        photo_link = self.grab_photo_link(cust_id)[0]

        print(self.delete_photo(photo_link, app))


        try:
            self.cursor.execute(f"Delete from customers where CUSTOMER_ID = {cust_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"

    # -----------------------------------------