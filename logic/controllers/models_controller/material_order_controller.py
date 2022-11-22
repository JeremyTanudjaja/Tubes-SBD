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

    def insert_new_material_order(self, data):
        """Inserting a new Material Order"""

        # SAVING Material Order DATA
        try:
            print("masuk insertion")
            self.cursor.execute(f"CALL OrderMaterial ('{data['Vendor_ID']}','{data['Material_ID']}','{data['Material_Name']}',"
                                f"'{data['Quantity']}','{data['Unit_Price']}', '{data['Date']}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    def update_material_order(self, id, data):
        """Update Material Order"""
        order_id = id
        # Check if Date is empty or not
        date = data['Date'].split(' ')[0]

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"CALL UpdOrder('{order_id}','{data['Vendor_ID']}','{data['Material_ID']}','{data['Material_Name']}',"
                                f"'{data['Quantity']}','{data['Unit_Price']}','{date}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"

    def delete_material_order(self, id):
        """Delete a Material Order From Reality"""

        order_id = id

        try:
            self.cursor.execute(f"Delete from material_orders where ORDER_ID = {order_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"