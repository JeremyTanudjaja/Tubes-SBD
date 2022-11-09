class Customer_Controller():

    def __init__(self, cursor):
        """Initialize the Customer controller"""
        print("connection to Customer succeeded")
        self.cursor = cursor

    def get_customer_data(self):
        """This Method will grab all the data from the Customer table"""
        data = []
        self.cursor.execute(
            f"select customer_id, customer_name, address, profile_image_link from customers")
        for customer_id, customer_name, address, profile_image_link in self.cursor:
            data.append({"customer_id": customer_id,
                         "customer_name": customer_name,
                         "address": address,
                         "image_link": profile_image_link})
        # print(data)
        print(len(data))
        return data