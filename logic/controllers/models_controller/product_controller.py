class Product_Controller():

    def __init__(self, cursor):
        """Initialize the Product controller"""
        print("connection to Product succeeded")
        self.cursor = cursor

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