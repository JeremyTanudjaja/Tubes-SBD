class Vendor_Controller():

    def __init__(self, cursor):
        """Initialize the Vendor controller"""
        print("connection to Vendor succeeded")
        self.cursor = cursor

    def get_vendor_data(self):
        """This Method will grab all the data from the vendor table"""
        data = []
        self.cursor.execute(
            f"select vendor_id, vendor_name, address "
            f"from Vendors")
        for vendor_id, vendor_name, address in self.cursor:
            data.append({"vendor_id": vendor_id,
                         "vendor_name": vendor_name,
                         "address": address})
        # print(data)
        print(len(data))
        return data