class Sales_Product_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Sales Product controller"""
        print("connection to Sales Product Database succeeded")
        self.cursor = cursor
        self.oracle = oracle

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
        print(len(data))
        return data


    def insert_new_sales_product(self, data):
        """Inserting a new product sales"""
        # SAVING sales product DATA
        try:
            print("masuk insertion")
            self.cursor.execute(f"CALL SalesProduct('{data['Customer_ID']}','{data['Product_ID']}','{data['Product_Name']}',"
                                f"'{data['Status']}','{data['Product_Quantity']}', '{data['Order_Date']}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    def update_sales_product(self, id, data):
        """Update Sales Product"""
        sales_id = id
        # Check if Date is empty or not
        date = data['Order_Date'].split(' ')[0]

        # Update Data
        try:
            print("masuk Update")
            self.cursor.execute(f"CALL UpdSales ('{sales_id}','{data['Customer_ID']}','{data['Product_ID']}','{data['Product_Name']}',"
                                f"'{data['Status']}','{data['Product_Quantity']}','{date}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"

    def delete_sales_product(self, id):
        """Delete a Sales Product From Reality"""
        sales_id = id
        try:
            self.cursor.execute(f"Delete from sales_products where SALES_ID = {sales_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"