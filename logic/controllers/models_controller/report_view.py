class Report_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Report controller"""
        print("connection to Report succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def AnnualDeptSal(self):
        """This Method will grab all the data from the Annual Dept View"""
        data = []
        self.cursor.execute(
            f"select dept_id , dept_name , annual_salary from vAnnualDeptSal")
        print(self.cursor)
        for dept_id , dept_name , annual_salary in self.cursor:
            data.append({"dept_id ": dept_id ,
                         "dept_name ": dept_name ,
                         "annual_salary": annual_salary})
        # print(data)
        print(len(data))
        return data

    def AverageSales(self):
        """This Method will grab all the data from the Average Sales View"""
        data = []
        self.cursor.execute(
            f"select customer_id , customer_name , average_buying from vSalesAvg")
        print(self.cursor)
        for customer_id, customer_name, average_buying in self.cursor:
            data.append({"customer_id": customer_id,
                         "customer_name": customer_name,
                         "average_buying": average_buying})
        # print(data)
        print(len(data))
        return data

    def OrderAvg(self):
        """This Method will grab all the data from the Order Average View"""
        data = []
        self.cursor.execute(
            f"select vendor_id, vendor_name, material_name, average_order from vOrderAvg")
        print(self.cursor)
        for vendor_id, vendor_name, material_name, average_order in self.cursor:
            data.append({"vendor_id": vendor_id,
                         "vendor_name": vendor_name,
                         "material_name": material_name,
                         "average_order": average_order})
        # print(data)
        print(len(data))
        return data

    def ProductSales(self):
        """This Method will grab all the data from the Product Sales View"""
        data = []
        self.cursor.execute(
            f"select product_name, total_unit_sales from vProductSales")
        print(self.cursor)
        for product_name, total_unit_sales in self.cursor:
            data.append({"product_name": product_name,
                         "Total_Unit_Sales": total_unit_sales
                        })
        # print(data)
        print(len(data))
        return data

    def ViewManager(self):
        """This Method will grab all the data from the View Manager View"""
        data = []
        self.cursor.execute(
            f"select dept_name, manager_id, full_name from vManager")
        print(self.cursor)
        for departmen_name, manager_id, full_name in self.cursor:
            data.append({"dept_name": departmen_name,
                         "manager_id": manager_id,
                         "full_name": full_name})
        # print(data)
        print(len(data))
        return data
