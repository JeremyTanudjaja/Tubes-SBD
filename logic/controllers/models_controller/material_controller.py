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