import os

import shortuuid
from werkzeug.utils import secure_filename


class Material_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Material controller"""
        print("connection to Material succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_material_data(self):
        """This Method will grab all the data from the material table"""
        data = []
        self.cursor.execute(
            f"select material_id, material_name, quantity, unit_price, material_picture_link, vendor_id "
            f"from vMaterials")
        for material_id, material_name, quantity, unit_price, material_picture_link, vendor_id in self.cursor:
            data.append({"material_id": material_id,
                         "material_name": material_name,
                         "quantity": quantity,
                         "unit_price": unit_price,
                         "image_link": material_picture_link,
                         "vendor_id": vendor_id})
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

    def insert_new_material(self, data, image, app):
        """Inserting a new Material"""

        # INSERTING THE FILENAME TO A FOLDER
        if image.filename == "":
            print("Image must have a filename")
            return "Error Image must have a filename"
        else:
            if not self.check_file_extension(image.filename, app):
                print("The Extension is not allowed")
                return "Image have bad extension type"
        filename = self.sanitize_file_name(image.filename)

        image.save(os.path.join(app.config['MATERIAL_IMAGE_UPLOADS'], filename))
        # SAVING MATERIAL DATA
        try:
            print("masuk insertion")
            self.cursor.execute(f"CALL newMaterials('{data['Material_Name']}','{data['Quantity']}',"
                                f"'{data['Material_Price']}','{filename}', '{data['Vendor_ID']}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    # ---------------------------------------------------------------

    def grab_photo_link(self, id):
        """Grab Photo Link from Material database"""
        mat_id = id
        link = None
        self.cursor.execute(f"select MATERIAL_PICTURE_LINK from materials where material_ID = {mat_id}")
        for photo_link in self.cursor:
            link = photo_link
        return link

    def delete_photo(self, photo_link, app):
        """Delete Photo from folder"""
        print(photo_link)
        try:
            os.remove(f"{app.config['MATERIAL_IMAGE_UPLOADS']}/{photo_link}")
        except FileNotFoundError as e:
            error_message = f"{e}"
            return error_message
        return "success delete"

    # UPDATE EMPLOYEES

    def update_material_data(self, id, image, data, app):
        """Update Material Data"""
        mat_id = id

        # Grab Old employee photo link
        photo_link = self.grab_photo_link(mat_id)[0]

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
            image.save(os.path.join(app.config['MATERIAL_IMAGE_UPLOADS'], filename))

            # Delete Old Photo if there's a new photo
            print(self.delete_photo(photo_link, app))

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"update materials set "
                                f"Material_NAME='{data['Material_Name']}',"
                                f"Quantity='{data['Quantity']}',"
                                f"Unit_Price='{data['Material_Price']}',"
                                f"MATERIAL_PICTURE_LINK='{filename}',"
                                f"VENDOR_ID='{data['Vendor_ID']}'"
                                f"where Material_ID={mat_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"

    # DELETION FUNCTIONS
    def delete_material(self, id, app):
        """Delete a Material From Reality"""
        # DELETE MATERIAL IMAGE
        material_id = id
        photo_link = self.grab_photo_link(material_id)[0]

        print(self.delete_photo(photo_link, app))

        try:
            self.cursor.execute(f"Delete from materials where material_ID = {material_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"

    # -----------------------------------------
