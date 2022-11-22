import os

import shortuuid
from werkzeug.utils import secure_filename


class Product_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Product controller"""
        print("connection to Product succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_product_data(self):
        """This Method will grab all the data from the product table"""
        data = []
        self.cursor.execute(
            f"select product_id, product_name, unit_price, product_image_link "
            f"from vProducts")
        for product_id, product_name, unit_price, product_image_link in self.cursor:
            data.append({"product_id": product_id,
                         "product_name": product_name,
                         "unit_price": unit_price,
                         "image_link": product_image_link})
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

    def insert_new_product(self, data, image, app):
        """Inserting a new Product"""

        # INSERTING THE FILENAME TO A FOLDER
        if image.filename == "":
            print("Image must have a filename")
            return "Error Image must have a filename"
        else:
            if not self.check_file_extension(image.filename, app):
                print("The Extension is not allowed")
                return "Image have bad extension type"
        filename = self.sanitize_file_name(image.filename)

        image.save(os.path.join(app.config['PRODUCT_IMAGE_UPLOADS'], filename))
        # SAVING MATERIAL DATA
        try:
            print("masuk insertion")
            self.cursor.execute(f"CALL newProduct('{data['Product_Name']}',"
                                f"'{data['Product_Price']}','{filename}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    # ---------------------------------------------------------------

    def grab_photo_link(self, id):
        """Grab Photo Link from Material database"""
        prod_id = id
        link = None
        self.cursor.execute(f"select PRODUCT_IMAGE_LINK from products where Product_ID = {prod_id}")
        for photo_link in self.cursor:
            link = photo_link
        return link

    def delete_photo(self, photo_link, app):
        """Delete Photo from folder"""
        print(photo_link)
        try:
            os.remove(f"{app.config['PRODUCT_IMAGE_UPLOADS']}/{photo_link}")
        except FileNotFoundError as e:
            error_message = f"{e}"
            return error_message
        return "success delete"

    # UPDATE EMPLOYEES

    def update_product_data(self, id, image, data, app):
        """Update Product Data"""
        prod_id = id

        # Grab Old product photo link
        photo_link = self.grab_photo_link(prod_id)[0]

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
            image.save(os.path.join(app.config['PRODUCT_IMAGE_UPLOADS'], filename))

            # Delete Old Photo if there's a new photo
            print(self.delete_photo(photo_link, app))

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"update products set "
                                f"PRODUCT_NAME='{data['Product_Name']}',"
                                f"UNIT_PRICE='{data['Product_Price']}',"
                                f"PRODUCT_IMAGE_LINK='{filename}'" 
                                f"where PRODUCT_ID={prod_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"

    # DELETION FUNCTIONS
    def delete_product(self, id, app):
        """Delete a Product From Reality"""
        # DELETE Product IMAGE
        prod_id = id
        photo_link = self.grab_photo_link(prod_id)[0]

        print(self.delete_photo(photo_link, app))

        try:
            self.cursor.execute(f"Delete from products where Product_ID = {prod_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"

    # -----------------------------------------
