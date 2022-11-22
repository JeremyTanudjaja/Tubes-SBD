class Inventory_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Inventory controller"""
        print("connection to Inventory succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_inventory_data(self):
        """This Method will grab all the data from the inventory table"""
        data = []
        self.cursor.execute(
            f"select product_id, product_name, quantity "
            f"from vInventories")
        for product_id, product_name, quantity in self.cursor:
            data.append({"product_id": product_id,
                         "product_name": product_name,
                         "quantity": quantity})
        # print(data)
        print(len(data))
        return data

    def insert_inventory(self, data):
        """Call Insert Inventory Procedure to Insert Data"""
        try:
            self.cursor.execute(f"CALL AddInven('{data['ID_Product']}','{data['Product_Name']}',{data['Product_Quantity']})")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"


    def update_inventory(self, id, data):
        """Update Inventory"""
        quantity = data['Quantity']
        prod_id = id
        try:
            self.cursor.execute(f"Update inventories set quantity={quantity}"
                                f"where Product_ID = {prod_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"


    def delete_inventory(self, id):
        """Delete a Inventory Item From Reality"""
        prod_id = id
        try:
            self.cursor.execute(f"Delete from inventories where Product_ID = {prod_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"

