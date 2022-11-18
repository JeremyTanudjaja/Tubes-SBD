class Material_Order_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Material Order controller"""
        print("connection to Material Order Database succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_material_order_data(self):
        """This Method will grab all the data from the Material Order table"""
        data = []
        self.cursor.execute(
            f"select order_id, vendor_id, material_id, material_name, quantity, unit_price, order_date "
            f"from vMaterialOrders")
        for order_id, vendor_id, material_id, material_name, quantity, unit_price, order_date in self.cursor:
            data.append({"order_id": order_id,
                         "vendor_id": vendor_id,
                         "material_id": material_id,
                         "material_name": material_name,
                         "quantity": quantity,
                         "unit_price": unit_price,
                         "order_date": order_date})
        # print(data)
        print(len(data))
        return data