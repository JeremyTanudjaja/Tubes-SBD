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