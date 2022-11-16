class Sales_Product_Controller():

    def __init__(self, cursor):
        """Initialize the Sales Product controller"""
        print("connection to Sales Product Database succeeded")
        self.cursor = cursor

    def get_sales_product_data(self):
        """This Method will grab all the data from the Sales Product table"""
        data = []
        self.cursor.execute(
            f"select sales_id, customer_id, product_id, product_name, status, quantity, order_date "
            f"from vSalesOrder")
        for sales_id, customer_id, product_id, product_name, status, quantity, order_date in self.cursor:
            data.append({"sales_id": sales_id,
                         "customer_id": customer_id,
                         "product_id": product_id,
                         "product_name": product_name,
                         "status": status,
                         "quantity": quantity,
                         "order_date": order_date})
        # print(data)
        print(len(data))
        return data